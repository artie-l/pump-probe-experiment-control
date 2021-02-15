from mttkinter import mtTkinter as tk
from tkinter import ttk

from gui.gui_variables import LIATconstVisual, LIASensVisual

class LIAControls(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)
        
        self.controller = controller

        self.parameters_LF = ttk.LabelFrame(self,
                                            text="LIA Parameters"
                                            )
        self.time_const_Label = ttk.Label(self.parameters_LF,
                                          text="Time constant"
                                          )
        self.time_const_Combobox = ttk.Combobox(self.parameters_LF,
                                                state="disabled",
                                                width=10
                                                )
        self.sens_Label = ttk.Label(self.parameters_LF,
                                    text="Sensitivity"
                                    )
        self.sens_Combobox = ttk.Combobox(self.parameters_LF,
                                          state="disabled",
                                          width=10
                                          )

        self.time_const_Combobox["values"] = LIATconstVisual
        self.sens_Combobox["values"] = LIASensVisual
        self.sens_Combobox.bind("<<ComboboxSelected>>",
                                self.change_sens
                                )
        self.time_const_Combobox.bind("<<ComboboxSelected>>",
                                      self.change_tconst
                                      )

        # Stick to Grid
        self.parameters_LF.grid(column=0, row=0,
                                )
        self.time_const_Label.grid(column=0, row=0
                                   )
        self.time_const_Combobox.grid(column=1, row=0,
                                      padx=5, pady=5
                                      )
        self.sens_Label.grid(column=0, row=1
                             )
        self.sens_Combobox.grid(column=1, row=1,
                                padx=5, pady=5
                                )

    def change_tconst(self, event):
        self.LIATimeConstParam = (LIATconstVisual.index(self.time_const_Combobox.get()))
        self.master.focus()
        self.controller.lia.set_tconst(self.LIATimeConstParam)

    def change_sens(self, event):
        self.LIASenstParam = (LIASensVisual.index(self.sens_Combobox.get()))
        self.master.focus()
        self.controller.lia.set_sens(self.LIASenstParam)
