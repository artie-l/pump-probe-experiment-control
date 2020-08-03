# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:56:14 2020

@author: XY
"""
from mttkinter import mtTkinter as tk
import ttk

from measurement_functions import convtomm
from gui_variables import DelayLines



class DelayLineControls(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent,)
        
        self.controller = controller

        self.delay_line_LF = ttk.LabelFrame(self, text="Delay Stage Control"
                                            )
        self.move_to_Button = ttk.Button(self.delay_line_LF,
                                         text="Move",
                                         state='disabled',
                                         command=self.move_to_Pos,
                                         )
        self.move_to_Entry = ttk.Entry(self.delay_line_LF,
                                       width=10,
                                       state="disabled"
                                       )
        self.move_to_Min_Button = ttk.Button(self.delay_line_LF,
                                             text="Min",
                                             state="disabled",
                                             command=self.move_to_Min,
                                             )
        self.move_to_Max_Button = ttk.Button(self.delay_line_LF,
                                             text="Max",
                                             state="disabled",
                                             command=self.move_to_Max
                                             )
        self.delay_line_name_Label = ttk.Label(self.delay_line_LF,
                                            text="Delay Line:"
                                            )
        self.delay_line_Combobox = ttk.Combobox(self.delay_line_LF,
                                                  state="disabled",
                                                  width=10,
                                                  )
        self.delay_line_Combobox["values"] = DelayLines
        self.delay_line_Combobox.bind("<<ComboboxSelected>>",
                                        self.change_delay_line
                                        )
        self.velocity_Entry = ttk.Entry(self.delay_line_LF,
                                        width=10,
                                        state="disabled"
                                        )
        self.set_velocity_Button = ttk.Button(self.delay_line_LF,
                                              text="Set Velocity",
                                              state='disabled',
                                              command=self.set_Velocity,
                                              )

        # Stick to grid
        self.delay_line_LF.grid(column=0, row=0,
                                padx=5
                                )
        self.move_to_Entry.grid(column=0, row=0,
                                )
        self.move_to_Button.grid(column=1, row=0)
        self.move_to_Min_Button.grid(column=0, row=1,
                                     padx=5, pady=5
                                     )
        self.move_to_Max_Button.grid(column=1, row=1,
                                     padx=5, pady=5
                                     )
        self.delay_line_name_Label.grid(column=0,row=2)
        self.delay_line_Combobox.grid(column=1, row=2,
                                      padx=5, pady=5
                                      )
        self.velocity_Entry.grid(column=0, row=3,
                                 padx=5, pady=5
                                 )
        self.set_velocity_Button.grid(column=1, row=3,
                                      padx=5, pady=5
                                      )
        
            
    def move_to_Max(self):
        self.controller.delay_line.move_to(self.controller.max_pos)
    
    def move_to_Min(self):
        self.controller.delay_line.move_to(self.controller.min_pos)
    
    def move_to_Pos(self):
        pos = convtomm(self.move_to_Entry.get())
        self.controller.delay_line.move_to(pos)
    
    def set_Velocity(self):
        velocity=float(self.velocity_Entry.get())
        self.controller.delay_line.set_velocity(velocity)
            
    def change_delay_line(self, event):
        self.delay_line_name=(self.delay_line_Combobox.get())
        self.master.focus()
        self.controller.positioner = str(self.delay_line_name)