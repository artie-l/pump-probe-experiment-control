# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:26:17 2020

@author: XY
"""

from mttkinter import mtTkinter as tk
import ttk
import tkMessageBox

import measurement_functions as mf
import Queue
import threading

from gui_logic import controls_on, controls_off, save_settings

def disable_event():
    tkMessageBox.showwarning('?!','Try again...')
    pass


def check_scan_direction(GUI):
    GUI = GUI.scan_parameters
    initialposition=float(GUI.initial_position_Entry.get())
    finalposition=float(GUI.final_position_Entry.get())
    step=float(GUI.step_Entry.get())
    number_of_scans=int(GUI.number_of_scans_Entry.get())
    if (finalposition-initialposition)/step > 0 and number_of_scans >0:
        return True
    else:
        return False

class QuickScanThread(threading.Thread):
    def __init__(self, queue, GUI):
        
        self.GUI = GUI
        
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        mf.fast_scan(self.GUI)
        self.queue.put("Task finished") # put smth in the queue 

class MeasurementThread(threading.Thread):
    def __init__(self, queue, GUI):
        
        self.GUI = GUI
        
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        self.GUI.min_pos, self.GUI.max_pos = mf.x_y_normal_scan(self.GUI)
        self.queue.put("Task finished") # put smth in the queue   


class ScanControls(tk.Frame):
    def __init__(self, parent, controller, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self.controller = controller
        
        self.current_scan_Var = tk.StringVar()
        self.end_scan_Var = tk.StringVar()

        self.scan_controls_LF = ttk.LabelFrame(self,
                                               text="Scan Initialization"
                                               )

        self.start_scan_Button = ttk.Button(self.scan_controls_LF,
                                            text="Start",
                                            state="disabled",
                                            command=self.start_scan
                                            )
        self.stop_scan_Button = ttk.Button(self.scan_controls_LF,
                                           text="Stop",
                                           state="disabled",
                                           command=self.stop_scan
                                           )
        self.quick_scan_Button = ttk.Button(self.scan_controls_LF,
                                            text="Quick Scan",
                                            state="disabled",
                                            command=self.quick_scan
                                            )
        self.pause_scan_Button = ttk.Button(self.scan_controls_LF,
                                            text="Pause",
                                            state="disabled",
                                            command=self.pause_scan
                                            )
        self.end_scan_Text = ttk.Label(self.scan_controls_LF,
                                       )
        self.end_scan_Label = ttk.Label(self.scan_controls_LF,
                                        textvariable=self.end_scan_Var
                                        )
        self.current_scan_Label = ttk.Label(self.scan_controls_LF,
                                            textvariable=self.current_scan_Var
                                            )

        self.scan_controls_LF.grid(column=0, row=0,
                                   )
        self.start_scan_Button.grid(column=0, row=0,
                                    ipady=10, ipadx=10,
                                    pady=10, padx=10
                                    )
        self.pause_scan_Button.grid(column=1, row=0,
                                    ipady=10, ipadx=10,
                                    pady=5, padx=5
                                    )
        self.stop_scan_Button.grid(column=2, row=0,
                                   ipady=10, ipadx=10,
                                   pady=5, padx=5
                                   )
        self.quick_scan_Button.grid(column=3, row=0,
                                    ipady=10, ipadx=10,
                                    pady=10, padx=10
                                    )
        self.end_scan_Text.grid(column=1, row=1,
                                padx=5, pady=5
                                )
        self.end_scan_Label.grid(column=2, row=1,
                                 padx=5, pady=5
                                 )
        self.current_scan_Label.grid(column=3, row=1,
                                     padx=5, pady=5
                                     )
        
        
    def start_scan(self):
        try:
            if check_scan_direction(self.controller):
                controls_off(self.controller)
                
                self.queueMeasurement = Queue.Queue() # put the task in the queue
                MeasurementThread(self.queueMeasurement, self.controller).start()
                self.master.after(100, self.measurement_queue)
                
                self.controller.master.protocol("WM_DELETE_WINDOW", disable_event) 
            else:
                tkMessageBox.showwarning('Incorrect Input values',
                                         'Check Initial,Final position and Step'
                                         )
        except ValueError:
            tkMessageBox.showwarning('Incorrect Input values',
                                     'Use dot, not comma. No symbols allowed'
                                     )
            
    def quick_scan(self):
        try:
            if check_scan_direction(self.controller):
                controls_off(self.controller)
                
                self.queueQuickScan = Queue.Queue() # put the task in the queue
                QuickScanThread(self.queueQuickScan, self.controller).start()
                self.master.after(100, self.quickscan_queue)
                
                self.controller.master.protocol("WM_DELETE_WINDOW", disable_event) 
            else:
                tkMessageBox.showwarning('Incorrect Input values',
                                         'Check Initial,Final position and Step'
                                         )
        except ValueError:
            tkMessageBox.showwarning('Incorrect Input values',
                                     'Use dot, not comma. No symbols allowed'
                                     )         
        
        
    def measurement_queue(self):
        try: #when queue is not empty do following
            msg = self.queueMeasurement.get(0)
            
            save_settings(self.controller)
            controls_on(self.controller)

            self.controller.master.protocol("WM_DELETE_WINDOW", self.controller.master.destroy)
            
        except Queue.Empty: #when queue is empty do smth
                self.master.after(100, self.measurement_queue)
                
    def quickscan_queue(self):
        try: #when queue is not empty do following
            msg = self.queueQuickScan.get(0)
            
            controls_on(self.controller)
            
            self.controller.master.protocol("WM_DELETE_WINDOW", self.controller.master.destroy)
        except Queue.Empty: #when queue is empty do smth
                self.master.after(100, self.quickscan_queue)
                
    def stop_scan(self):
        self.stop_scan_Button.configure(state="disabled")#disable the button
        if str(self.pause_scan_Button['text']) == 'Resume':
            self.pause_scan_Button.configure(text='Pause')
            self.pause_scan_Button.configure(state='disabled')
        self.pause_scan_Button.configure(state='disabled')
         
    def pause_scan(self):
        if str(self.pause_scan_Button['text']) == 'Pause':
            self.pause_scan_Button.configure(text='Resume')
        else:
           self.pause_scan_Button.configure(text='Pause') 
