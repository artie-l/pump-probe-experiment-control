import numpy as np
from gui.gui_variables import tconstliaoutp, tconstuseroutp
import datetime
import time
from pyautogui import press
from PIL import ImageGrab


def convtomm(var):
    try:
        mm = np.float64(var) * (1 / ((10 ** (-3)) / 299792458 * 10 ** (12) * 2))
        return mm
    except ValueError:
        return 0


def convtops(var):
    ps = np.float64(var) * (10 ** (-3)) / 299792458 * 10 ** (12) * 2;
    return ps


def x_y_normal_scan(GUI):
    # Setting up the UI
    GUI.scan_PB["value"] = 0
    GUI.scan_controls.end_scan_Text['text'] = 'Approx. ending time:'
    GUI.rt_LIA.trigger_Button['text'] = 'Start'

    stop_button = GUI.scan_controls.stop_scan_Button
    pause_button = GUI.scan_controls.pause_scan_Button

    stop_button['state'] = '!disabled'
    pause_button['state'] = '!disabled'

    # Collecting values from GUI
    init_pos = convtomm(GUI.scan_parameters.initial_position_Entry.get())
    fin_pos = convtomm(GUI.scan_parameters.final_position_Entry.get())
    step = convtomm(GUI.scan_parameters.step_Entry.get())
    nbrofscans = int(GUI.scan_parameters.number_of_scans_Entry.get())
    delay = np.arange(init_pos, fin_pos, step)
    delayps = convtops(delay)

    theday = datetime.date.today().strftime('%d_%m_%Y')
    daily_scan_number = GUI.file_path_name_entries.scan_number_Var.get()
    folder = GUI.file_path_name_entries.folder_path_Entry.get()
    filename = GUI.file_path_name_entries.file_name_Entry.get()

    lia = GUI.lia

    # get the correct waiting time required for the LIA integration
    tconst = lia.get_tconst()
    tconstarraynum = np.where(tconstliaoutp == tconst)[0][0]
    waittime = 3 * tconstuseroutp[tconstarraynum]

    # Estimation of the scan time
    if nbrofscans <= 500:
        scan_duration = int(nbrofscans * (
                waittime * ((fin_pos - init_pos) / step + 10)
                + ((fin_pos - init_pos) / step) * 0.062 + 1.2)
                            )
        scan_end_time = str(datetime.datetime.now() + datetime.timedelta(seconds=scan_duration))[5:-7]
        GUI.scan_controls.end_scan_Var.set(scan_end_time)
    else:
        GUI.scan_controls.end_scan_Var.set('Really long')

    # Creating the all file to write data inside
    with open(folder + theday + '_' + filename + '_all_' + daily_scan_number + '_X.txt', 'w+') as f:  # Write allfile
        np.savetxt(f, delayps, fmt='%s', delimiter='\t')
        
    with open(folder + theday + '_' + filename + '_all_' + daily_scan_number + '_Y.txt', 'w+') as f:  # Write allfile
        np.savetxt(f, delayps, fmt='%s', delimiter='\t')

    # Setting up the loop control variables
    currentscan = 1

    xscansarray = []
    yscansarray = []

    GUI.current_scan_PB['maximum'] = len(delay)
    GUI.scan_PB['maximum'] = nbrofscans

    # Measurement start 
    while currentscan <= nbrofscans and stop_button['state'] == '!disabled':

        datax = []
        datay = []

        GUI.delay_line.move_to(delay[0])
        time.sleep(0.02)

        # LIA initialization
        # We should sleep for 20 ms at least after each write command to avoid interference
        lia.start_acqusition()

        for index, value in enumerate(delay):
            GUI.current_scan_PB["value"] = index
            GUI.delay_line.move_to(value)
            time.sleep(waittime)
            lia.trigger()

        # Getting data from LIA
        bufferlength = lia.get_buffer_len()

        datax = (lia.get_channel_one(bufferlength).replace("\n", "").replace("\r", "").split(',')[0:bufferlength])

        datay = (lia.get_channel_two(bufferlength).replace("\n", "").replace("\r", "").split(',')[0:bufferlength])

        # Appending the data arrays with measured points
        xscansarray.append(datax)
        yscansarray.append(datay)

        GUI.scan_controls.current_scan_Var.set('Scan Number ' + str(currentscan))
        GUI.scan_PB["value"] = currentscan

        # Append measured data to an all_scans file
        with open(folder + theday + '_' + filename + '_all_' + daily_scan_number + '_X.txt', 'r+') as f:
            data = np.loadtxt(f, dtype=float, delimiter='\t')
            f.seek(0)
            f.truncate(0)
            np.savetxt(f, np.column_stack((data, datax)), fmt='%s', delimiter='\t')
            
        with open(folder + theday + '_' + filename + '_all_' + daily_scan_number + '_Y.txt', 'r+') as f:
            data = np.loadtxt(f, dtype=float, delimiter='\t')
            f.seek(0)
            f.truncate(0)
            np.savetxt(f, np.column_stack((data, datay)), fmt='%s', delimiter='\t')

        # Plotting the data
        data_plot(delayps, xscansarray, GUI.fig_x_channel, GUI.toolbar_x, GUI)
        data_plot(delayps, yscansarray, GUI.fig_y_channel, '', GUI)
        data_plot(delayps, xscansarray, GUI.fig_fft, '', GUI, 'plot')

        # Check if we want to pause

        while pause_button['text'] == 'Resume':
            pass

        currentscan += 1

    # calculating the average of all scans
    xmeandata = np.mean(np.array(xscansarray).astype(np.float), axis=0)
    ymeandata = np.mean(np.array(yscansarray).astype(np.float), axis=0)

    # Saving the mean_scan.txt file and images

    with open(folder + theday + '_' + filename + '_mean_' + str(daily_scan_number) + '_X.txt',
              'w+') as f:  # Write meanfile
        np.savetxt(f, np.column_stack((delayps, xmeandata)), fmt='%s', delimiter='\t');

    with open(folder + theday + '_' + filename + '_mean_' + str(daily_scan_number) + '_Y.txt',
              'w+') as f:  # Write meanfile
        np.savetxt(f, np.column_stack((delayps, ymeandata)), fmt='%s', delimiter='\t');

    # Saving the plots

    GUI.fig_x_channel.savefig(folder + theday + '_' + filename + '_mean_' + str(daily_scan_number) + '_X.png',
                              dpi=150, facecolor='w', edgecolor='w',
                              orientation='portrait', format=None,
                              transparent=True, bbox_inches='tight'
                              )
    GUI.fig_y_channel.savefig(folder + theday + '_' + filename + '_mean_' + str(daily_scan_number) + '_Y.png',
                              dpi=150, facecolor='w', edgecolor='w',
                              orientation='portrait', format=None,
                              transparent=True, bbox_inches='tight'
                              )

    # cleaning UI

    GUI.scan_controls.end_scan_Var.set('')
    GUI.scan_controls.end_scan_Text['text'] = ''
    GUI.scan_controls.current_scan_Var.set('')
    GUI.current_scan_PB['value'] = 0
    GUI.scan_PB['value'] = 0
    
    # saving up the screenshot of the GUI
    GUI.parent.attributes("-topmost", True)
    GUI.parent.after_idle(GUI.parent.attributes,'-topmost',False)
    press('printscreen')
    ImageGrab.grabclipboard().save(folder + theday + '_' + filename + '_screenshot_' + str(daily_scan_number) + '.png','PNG')

    # appending scan number

    daily_scan_number = int(daily_scan_number) + 1
    GUI.file_path_name_entries.scan_number_Var.set(str(daily_scan_number))

    # looking for min and max position

    min_pos_index = np.argmin(xmeandata)
    max_pos_index = np.argmax(xmeandata)

    return delay[min_pos_index], delay[max_pos_index]


# Fast scan, used for alignment. No data will be taken

def fast_scan(GUI):
    # Setting up the UI

    stop_button = GUI.scan_controls.stop_scan_Button
    pause_button = GUI.scan_controls.pause_scan_Button
    GUI.rt_LIA.trigger_Button['state'] = '!disabled'

    stop_button['state'] = '!disabled'
    pause_button['state'] = '!disabled'

    lia = GUI.lia

    # Collecting values from GUI

    init_pos = convtomm(GUI.scan_parameters.initial_position_Entry.get())
    fin_pos = convtomm(GUI.scan_parameters.final_position_Entry.get())
    step = convtomm(GUI.scan_parameters.step_Entry.get())
    delay = np.arange(init_pos, fin_pos, step)

    # get the correct waiting time required for the LIA integration

    tconst = lia.get_tconst()
    tconstarraynum = np.where(tconstliaoutp == tconst)[0][0]
    waittime = 3 * tconstuseroutp[tconstarraynum]

    # Setting up the loop control variables

    GUI.current_scan_PB['maximum'] = len(delay)

    while stop_button['state'] == '!disabled':

        GUI.delay_line.move_to(delay[0])

        for index, value in enumerate(delay):
            GUI.current_scan_PB["value"] = index
            GUI.delay_line.move_to(value)
            time.sleep(waittime)

        while pause_button['text'] == 'Resume':
            pass

    GUI.current_scan_PB["value"] = 0
    GUI.rt_LIA.trigger_Button['text'] = 'Start'


def data_plot(x_data, y_data, figure, toolbar, GUI, msg=''):
    axes = figure.get_axes()
    y_data = np.array(y_data).astype(np.float)
    y_data_mean = np.mean(y_data, axis=0)

    y_data = y_data[-1, :]

    if len(axes) == 2:
        axes[0].clear()
        axes[1].clear()

        axes[0].plot(x_data, y_data * 1E6, 'xkcd:crimson', label='Last scan', )
        axes[0].plot(x_data, y_data_mean * 1E6, 'xkcd:blue', label='Avg Scan', )
        axes[0].legend()

        twin_axes_ticks = []
        ticks = axes[0].get_xticks()
        for tick in ticks:
            twin_axes_ticks.append(round(convtomm(tick), 1))

        axes[1].set_xticks(ticks)
        axes[1].set_xbound(axes[0].get_xbound())
        axes[1].set_xticklabels(twin_axes_ticks)

        axes[0].set_xlabel('Time delay, ps')
        axes[0].set_ylabel('Signal, $\mu$V')
        axes[1].set_xlabel('Delay Line Pos, mm')

        axes[1].set_zorder(0)
        axes[0].set_zorder(1)

        if x_data[0] > x_data[1]:
            axes[0].invert_xaxis()
            axes[1].invert_xaxis()

        if toolbar != '':
            toolbar.update()

        figure.tight_layout()
    else:
        axes[0].clear()

        y_data_mean = y_data_mean - np.mean(y_data_mean[0:25])

        fft_data = np.abs(np.fft.fft(y_data_mean))
        fft_freq = np.fft.fftfreq(len(y_data_mean), x_data[1] - x_data[0])

        axes[0].plot(fft_freq, fft_data / np.max(fft_data), scaley=False, scalex=False)
        axes[0].set_xlim(0, 5)
        axes[0].set_xlabel('Frequency, THz')
        axes[0].set_ylabel('FFT Amplitude')

    GUI.plot_queue.put(msg)
