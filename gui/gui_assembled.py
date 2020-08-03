from mttkinter import mtTkinter as tk
import ttk
import tkMessageBox

from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from matplotlib.figure import Figure

from gui_scan_controls import ScanControls
from gui_scan_params import ScanParameters
from gui_filepath_entries import FilePathNameEntriess
from gui_lia_controls import LIAControls
from gui_delay_line_controls import DelayLineControls
from gui_data_graphs import DataGraphs
from gui_rt_lia import RealTimeLIAValues
from gui_chopper_controls import ChopperControls

from gui_logic import gui_init, gui_stop
import tools_initialization as ti




class GUI(tk.Frame):
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        self.parent = parent
        self.parent.title("Manip Control")
        self.parent.iconbitmap('misc/laser-logo.ico') 
        
        # Initiaizing figures
        self.fig_x_channel = Figure(figsize=(6, 3.7), dpi=100)
        self.fig_x_channel.add_subplot(111).twiny()

        self.fig_y_channel = Figure(figsize=(6, 3.7), dpi=100)
        self.fig_y_channel.add_subplot(111).twiny()

        self.fig_fft = Figure(figsize=(6, 3.7), dpi=100)
        self.fig_fft.add_subplot(111)
        

        # Button to check if everything is connected, to unlock GUI
        self.InitializeButton = tk.Button(self.parent, text="Initialize",
                                          height=5, width=25,
                                          bd=5,
                                          bg="green", activebackground="green",
                                          command=self.Initialize_programm,)

        self.scan_PB = ttk.Progressbar(self.parent,
                                       orient="horizontal",
                                       length=475,
                                       mode="determinate",
                                       )

        self.current_scan_PB = ttk.Progressbar(self.parent,
                                               orient="horizontal",
                                               length=125,
                                               mode="determinate",
                                               )

        # Initialize all necessary control elements
        self.file_path_name_entries = FilePathNameEntries(parent)
        self.graph_space = DataGraphs(parent, self)
        self.rt_LIA = RealTimeLIAValues(parent)
        self.scan_parameters = ScanParameters(parent)
        self.delay_line_controls = DelayLineControls(parent, self)
        self.scan_controls = ScanControls(parent, self)
        self.lia_controls = LIAControls(parent, self)
        self.chopper_controls = ChopperControls(parent, self)
        
        # Create a Toolbar fot X graph
        self.toolbar_x = NavigationToolbar2Tk(self.graph_space.canvas_x,
                                              self.graph_space.toolbar_X_Frame
                                              )
        self.toolbar_x.update()

        # Stick all elements to the grid
        self.InitializeButton.grid(column=0, row=0,
                                   # columnspan=2, rowspan=2,
                                   padx=10
                                   )
        self.file_path_name_entries.grid(column=2, row=0, )
        self.graph_space.grid(column=5, row=0,
                              columnspan=2, rowspan=12,
                              )
        self.scan_PB.grid(column=2, row=1,
                          ipady=10, padx=5
                          )
        self.current_scan_PB.grid(column=2, row=1,
                                  ipady=3, padx=5
                                  )
        self.rt_LIA.grid(column=2, row=2,
                         rowspan=5
                         )
        self.scan_parameters.grid(column=0, row=3, )
        self.delay_line_controls.grid(column=0, row=4, )
        self.lia_controls.grid(column=0, row=5, )
        self.chopper_controls.grid(column=0, row=6, )
        self.scan_controls.grid(column=1, row=11,
                                columnspan=2,
                                )

    def Initialize_programm(self):
        if self.InitializeButton['text'] == "Initialize":
            try:
                # Checking connection to LIA
                self.lia = ti.LIA()
                self.lia.get_idn()
                try:
                    # Checking connection to delay line
                    self.delay_line = ti.DelayLine(self)
                    gui_init(self)
                except SystemExit:
                    tkMessageBox.showerror('ERROR', 'Connection to XPS failed, check IP, Portand Power')
            except IOError:
                with open('misc/settings.txt', 'a+'):
                    tkMessageBox.showerror('No file with settigns', 'Created a new one in root directory')
            except:
                tkMessageBox.showerror('ERROR', 'Check the LIA connection and alimentation')
        else:
            gui_stop(self)
            pass


