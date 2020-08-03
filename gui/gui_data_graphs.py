# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:01:06 2020

@author: XY
"""

from mttkinter import mtTkinter as tk
import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class DataGraphs(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        
        self.controller = controller
        
        # Create the GUI for the plot space
        self.x_channel_LF = ttk.LabelFrame(self,
                                           text="Channel X"
                                           )
        self.y_channel_LF = ttk.LabelFrame(self,
                                           text="Complementary Info"
                                           )
        self.graph_space_X_Frame = ttk.Frame(self.x_channel_LF,
                                             borderwidth=5,
                                             )
        self.toolbar_X_Frame = ttk.Frame(self.x_channel_LF,
                                         borderwidth=5,
                                         )
        self.graph_space_Y_FFT_Notebook = ttk.Notebook(self.y_channel_LF
                                                       )
        self.graph_space_Y_Frame = ttk.Frame(self.graph_space_Y_FFT_Notebook,
                                             )
        self.graph_space_FFT_Frame = ttk.Frame(self.graph_space_Y_FFT_Notebook,
                                               )

        # Adding pages to notebook
        self.graph_space_Y_FFT_Notebook.add(self.graph_space_Y_Frame,
                                            text='Channel Y'
                                            )
        self.graph_space_Y_FFT_Notebook.add(self.graph_space_FFT_Frame,
                                            text='FFT'
                                            )

        # Plotting figures on the canvas
        self.canvas_x = FigureCanvasTkAgg(self.controller.fig_x_channel,
                                          master=self.graph_space_X_Frame
                                          )
        self.canvas_y = FigureCanvasTkAgg(self.controller.fig_y_channel,
                                          master=self.graph_space_Y_Frame
                                          )
        self.canvas_fft = FigureCanvasTkAgg(self.controller.fig_fft,
                                            master=self.graph_space_FFT_Frame
                                            )

        # Stick it to the grid
        self.x_channel_LF.grid(column=0, row=0,
                               padx=10, pady=10
                               )
        self.graph_space_X_Frame.grid(column=0, row=0,
                                      )
        self.toolbar_X_Frame.grid(column=0, row=1
                                  )
        self.y_channel_LF.grid(column=0, row=1,
                               padx=10, pady=10
                               )
        self.graph_space_Y_FFT_Notebook.grid(column=0, row=1,
                                             )
        self.canvas_x.get_tk_widget().grid(column=0, row=0,
                                           )
        self.canvas_y.get_tk_widget().grid(column=0, row=0,
                                           )
        self.canvas_fft.get_tk_widget().grid(column=0, row=0,
                                             )

        # Drawing figures
        self.canvas_x.draw()
        self.canvas_y.draw()
        self.canvas_fft.draw()