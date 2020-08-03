# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:22:56 2020

@author: XY
"""

from mttkinter import mtTkinter as tk
import ttk  



class ScanParameters(tk.Frame):
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self.scan_parameters_LF = ttk.LabelFrame(self,
                                                 text="Scan Parameters"
                                                 )
        self.initial_position_Label = ttk.Label(self.scan_parameters_LF,
                                                text="Initial Position (ps):",
                                                )

        self.initial_position_Entry = ttk.Entry(self.scan_parameters_LF, width=10,
                                                state="disabled",
                                                )

        self.final_position_Label = ttk.Label(self.scan_parameters_LF,
                                              text="Final Position (ps):"
                                              )

        self.final_position_Entry = ttk.Entry(self.scan_parameters_LF,
                                              width=10,
                                              state="disabled"
                                              )

        self.step_Label = ttk.Label(self.scan_parameters_LF,
                                    text="Step (ps):"
                                    )

        self.step_Entry = ttk.Entry(self.scan_parameters_LF,
                                    width=10,
                                    state="disabled"
                                    )

        self.scan_number_Label = ttk.Label(self.scan_parameters_LF,
                                           text="Number of Scans:"
                                           )

        self.number_of_scans_Entry = ttk.Entry(self.scan_parameters_LF,
                                           width=10,
                                           state="disabled"
                                           )

        # Stick to grid
        self.scan_parameters_LF.grid(column=0, row=0,
                                     padx=5
                                     )
        self.initial_position_Label.grid(column=0, row=0
                                         )
        self.initial_position_Entry.grid(column=1, row=0,
                                         padx=7, pady=5
                                         )
        self.final_position_Label.grid(column=0, row=1
                                       )
        self.final_position_Entry.grid(column=1, row=1,
                                       padx=7, pady=5
                                       )
        self.step_Label.grid(column=0, row=2
                             )
        self.step_Entry.grid(column=1, row=2,
                             padx=7, pady=5
                             )
        self.scan_number_Label.grid(column=0, row=3
                                    )
        self.number_of_scans_Entry.grid(column=1, row=3,
                                    padx=7, pady=5
                                    )