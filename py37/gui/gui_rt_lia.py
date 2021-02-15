from mttkinter import mtTkinter as tk
from tkinter import ttk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from numpy import arange


class RealTimeLIAValues(tk.Frame):
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self.traces = dict()

        # Define matplotlib figure
        self.f = Figure(figsize=(4.5, 3), dpi=100)
        self.a = self.f.add_subplot(111)
        self.f.set_tight_layout(True)
        

        # create arrays to plot the values
        self.y = [0] * 50
        self.x = arange(0, 50, 1)
        self.i = 0

        # Create the GUI for the live readings from LIA
        self.real_time_LIA_values_LF = ttk.LabelFrame(self,
                                                      text="LIA Output, R"
                                                      )
        self.values_Frame = ttk.Frame(self.real_time_LIA_values_LF,
                                      borderwidth=5,
                                      )
        self.trigger_Button = ttk.Button(self.real_time_LIA_values_LF,
                                         text='Start',
                                         state='disabled',
                                         command=self.on_off
                                         )

        # Stick it to the grid
        self.real_time_LIA_values_LF.grid(column=0, row=0,
                                          padx=5
                                          )
        self.values_Frame.grid(column=0, row=0,
                               )
        self.trigger_Button.grid(column=0, row=2,
                                 pady=7
                                 )

        # Create, stick and draw canvas for the figure
        self.canvas = FigureCanvasTkAgg(self.f, master=self.values_Frame)
        self.canvas.get_tk_widget().grid(column=0, row=0, )
        self.canvas.draw()

    # Change the name of the button, need for the animation
    def on_off(self):
        if self.trigger_Button['text'] == "Stop":
            self.trigger_Button['text'] = "Start"
        else:
            self.trigger_Button['text'] = "Stop"

    # Trace the line
    def trace(self, name, dataset_x, dataset_y):
        if name in self.traces:
            self.line1.set_data(dataset_x, dataset_y)
            data = self.line1.get_ydata()
            self.a.set_ylim(min(data), max(data))
        else:
            self.traces[name] = True
            self.line1, = self.a.plot(dataset_x, dataset_y)
        self.canvas.draw()
