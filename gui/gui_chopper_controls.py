# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 13:05:46 2020

@author: XY
"""
from mttkinter import mtTkinter as tk
import ttk

from gui_variables import ChopperFrequencyPreset, LIAChopperOutpValues


class ChopperControls(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        
        self.controller = controller
        
        self.chopper_controls_LF = ttk.LabelFrame(self,
                                                 text="Chopper Frequency"   
                                                 )
        self.frequency_Label = ttk.Label(self.chopper_controls_LF,
                                         text="Frequency"
                                         )
        
        self.frequency_Combobox = ttk.Combobox(self.chopper_controls_LF,
                                               width=10,
                                               state="disabled",
                                               )
        
        # Stick to grid
        self.chopper_controls_LF.grid(column=0, row=0,
                                      )
        self.frequency_Label.grid(column=0,row=0)
        self.frequency_Combobox.grid(column=1,row=0,
                                     padx=5,pady=5
                                     )
        
        self.frequency_Combobox["values"]=ChopperFrequencyPreset
        self.frequency_Combobox.bind("<<ComboboxSelected>>", self.change_frequency)
        
    def change_frequency(self, event):
        self.ChosenChopperFrequency=(ChopperFrequencyPreset.index(self.frequency_Combobox.get()))
        self.master.focus()
        self.controller.lia.set_auxv2(LIAChopperOutpValues[self.ChosenChopperFrequency])