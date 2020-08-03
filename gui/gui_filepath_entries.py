# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 12:50:34 2020

@author: XY
"""

from mttkinter import mtTkinter as tk
import ttk
import tkFileDialog

class FilePathNameEntries(tk.Frame):
    def __init__(self, parent, **kwargs):
        tk.Frame.__init__(self, parent, **kwargs)

        self.scan_number_Var = tk.StringVar()
        
        self.photo=tk.PhotoImage(master=self,file="misc/folder.gif")
        # Creating the GUI elements
        self.path_file_entries_LF = ttk.LabelFrame(self,
                                                   text="Path and File Name",
                                                   )
        self.folder_Label = ttk.Label(self.path_file_entries_LF,
                                      text="Folder:",
                                      )
        self.folder_path_Entry = ttk.Entry(self.path_file_entries_LF,
                                           width=30,
                                           state="disabled",
                                           )
        self.folder_path_choose_Button = tk.Button(self.path_file_entries_LF,
                                                   height=15, width=20,
                                                   state="disabled",
                                                   command=self.get_folder_path,
                                                   image=self.photo,
                                                   )
        self.file_name_Label = ttk.Label(self.path_file_entries_LF,
                                         text="File name:"
                                         )
        self.file_name_Entry = ttk.Entry(self.path_file_entries_LF,
                                         width=30,
                                         state="disabled",
                                         )
        self.scan_number_Label = ttk.Label(self.path_file_entries_LF,
                                           textvariable=self.scan_number_Var
                                           )

        # Sticking to the grid
        self.path_file_entries_LF.grid(column=0, row=0,
                                       columnspan=3, rowspan=2,
                                       padx=5, pady=5
                                       )
        self.folder_Label.grid(column=0, row=0)
        self.folder_path_Entry.grid(column=1, row=0,
                                    padx=5, pady=5,
                                    )
        self.folder_path_choose_Button.grid(column=2, row=0,
                                            padx=5,
                                            )
        self.file_name_Label.grid(column=0, row=1)
        self.file_name_Entry.grid(column=1, row=1,
                                  padx=5, pady=5
                                  )
        self.scan_number_Label.grid(column=2, row=1,
                                    padx=5, pady=5
                                    )
        
    def get_folder_path(self):
        self.directory = tkFileDialog.askdirectory()
        if self.directory != '':
            self.folder_path_Entry.delete(0, 'end')
            self.folder_path_Entry.insert(0, (self.directory +'/'))