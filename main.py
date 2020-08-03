# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 17:24:10 2020

@author: XY
"""



import gui.gui_assembled as gui


from mttkinter import mtTkinter as tk



if __name__ == "__main__":
    root = tk.Tk()
    main_ui = gui.GUI(root)
    
        
    def update():
        
        # Checking the index of currently measured point:
        if main_ui.rt_LIA.trigger_Button['text'] == "Stop":
            # Getting the value from LIA
            main_ui.rt_LIA.y.append(main_ui.lia.get_R()*10**6)
            # Re-plotting the curve
            main_ui.rt_LIA.y = main_ui.rt_LIA.y[1:]
            main_ui.rt_LIA.trace("test", main_ui.rt_LIA.x, main_ui.rt_LIA.y)
            # Moving to the next point
            main_ui.rt_LIA.i += 1

        root.after(25, update)


    update()

    root.mainloop()