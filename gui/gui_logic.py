# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:00:27 2018

@author: artml
"""

from datetime import date
from numpy import savetxt

from gui_variables import LIATconstVisual, LIASensVisual, ChopperFrequencyPreset, LIAChopperOutpValues


def enable(frame, state='!disabled'):
    def c_state(widget):
        # Is this widget a container?
        if widget.winfo_children:
            # It's a container, so iterate through its children
            for w in widget.winfo_children():
                try:
                    # change its state
                    w.state((state,))
                    # and then recurse to process ITS children
                    c_state(w)
                except AttributeError:
                    if state == '!disabled':
                        w['state'] = 'normal'
                    else:
                        w['state'] = state

    c_state(frame)

def disable(frame):
    enable(frame, 'disabled')

def save_settings(GUI):
    try:
        GUI.positioner
    except AttributeError:
        GUI.positioner = ''

    Parameters=[GUI.file_path_name_entries.folder_path_Entry.get(),
                GUI.file_path_name_entries.file_name_Entry.get(),
                date.today().strftime('%d_%m_%Y'),
                GUI.file_path_name_entries.scan_number_Var.get(),
                      
                GUI.scan_parameters.initial_position_Entry.get(),
                GUI.scan_parameters.final_position_Entry.get(),
                GUI.scan_parameters.step_Entry.get(),
                GUI.scan_parameters.number_of_scans_Entry.get(),
                      
                GUI.lia.get_tconst(),
                GUI.lia.get_sens(),
                      
                GUI.positioner
             ]
    
    with open('misc/settings.txt','wb') as f:   #Write allfile
            savetxt(f,Parameters,fmt='%s',delimiter='\t');
            
def daily_check(theday):
    today = date.today().strftime('%d_%m_%Y')
    if theday != today:
        daily_scan_number = 0;
    else:
        with open('misc/settings.txt', 'r') as f:
            daily_scan_number = f.readlines()[3].replace("\n", "")
    return daily_scan_number


# Enabling UI elements
def controls_on(GUI):
    enable(GUI.file_path_name_entries)
    enable(GUI.rt_LIA)
    enable(GUI.scan_parameters)
    enable(GUI.delay_line_controls)
    enable(GUI.lia_controls)
    enable(GUI.scan_controls)
    GUI.scan_controls.stop_scan_Button['state'] = 'disabled'
    GUI.scan_controls.pause_scan_Button['state'] = 'disabled'
    enable(GUI.chopper_controls)
    if GUI.InitializeButton['text'] == 'Stop':
        GUI.InitializeButton['state'] = 'normal'

# Disabling UI elements    
def controls_off(GUI):
    disable(GUI.file_path_name_entries)
    disable(GUI.rt_LIA)
    disable(GUI.scan_parameters)
    disable(GUI.delay_line_controls)
    disable(GUI.lia_controls)
    disable(GUI.scan_controls)
    disable(GUI.chopper_controls)
    if GUI.InitializeButton['text'] == 'Stop':
        GUI.InitializeButton['state'] = 'disabled'
    
    
def gui_init(GUI):
    
    # Setting up GUI elements
    GUI.InitializeButton.configure(text="Stop",bg="red",activebackground="red")
    
    # Enabling UI elements
    controls_on(GUI)
    
    GUI.chopper_controls.frequency_Combobox['state'] = "readonly"    
    GUI.lia_controls.sens_Combobox['state'] = "readonly"
    GUI.lia_controls.time_const_Combobox['state'] = "readonly"
    GUI.delay_line_controls.delay_line_Combobox['state'] = "readonly"
    GUI.file_path_name_entries.scan_number_Var.set('0')

    
    with open('misc/settings.txt', 'r') as f:
        Params = f.readlines()
        Params = [item.replace("\n", "") for item in Params]
    if len(Params) == 11:
        # Recalling previously saved parameters        
        GUI.file_path_name_entries.folder_path_Entry.insert(0,Params[0])
        GUI.file_path_name_entries.file_name_Entry.insert(0,Params[1])
        GUI.file_path_name_entries.scan_number_Var.set(daily_check(Params[2]))
        # we save scannumber var as Params[3]
        
        GUI.scan_parameters.initial_position_Entry.insert(0,Params[4])
        GUI.scan_parameters.final_position_Entry.insert(0,Params[5])
        GUI.scan_parameters.step_Entry.insert(0,Params[6])
        GUI.scan_parameters.number_of_scans_Entry.insert(0,Params[7])
        
        GUI.lia_controls.time_const_Combobox.set(LIATconstVisual[int(Params[8])])
        GUI.lia.set_tconst(Params[8])
        GUI.lia_controls.sens_Combobox.set(LIASensVisual[int(Params[9])])
        GUI.lia.set_sens(Params[9])
        
        GUI.delay_line_controls.delay_line_Combobox.set(Params[10])
        GUI.positioner = Params[10]
        
        GUI.chopper_controls.frequency_Combobox.set(ChopperFrequencyPreset[1])
        GUI.lia.set_auxv2(LIAChopperOutpValues[1])
        
        
    # Disabling unnecessery elements 
    GUI.delay_line_controls.move_to_Max_Button['state'] = 'disabled'
    GUI.delay_line_controls.move_to_Min_Button['state'] = 'disabled'
        
     
def gui_stop(GUI):
    
    GUI.InitializeButton.configure(text="Initialize", bg="green",activebackground="green")
    
    save_settings(GUI)
    
    GUI.file_path_name_entries.folder_path_Entry.delete(0, 'end')
    GUI.file_path_name_entries.file_name_Entry.delete(0, 'end')
    GUI.file_path_name_entries.scan_number_Var.set("")
    
    GUI.scan_parameters.initial_position_Entry.delete(0, 'end')
    GUI.scan_parameters.final_position_Entry.delete(0, 'end')
    GUI.scan_parameters.step_Entry.delete(0, 'end')
    GUI.scan_parameters.number_of_scans_Entry.delete(0, 'end')
    
    GUI.lia_controls.time_const_Combobox.set("")
    GUI.lia_controls.sens_Combobox.set("")
    
    GUI.chopper_controls.frequency_Combobox.set("")
    
    controls_off(GUI)
    
