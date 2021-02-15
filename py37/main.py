
from os.path import dirname, abspath, join
import sys
# Find code directory relative to our directory
THIS_DIR = dirname(__file__)
CODE_DIR = abspath(join(THIS_DIR, '..', 'code'))
sys.path.append(CODE_DIR)

import gui.gui_assembled as gui
from mttkinter import mtTkinter as tk

import queue

callback_queue = queue.Queue()


if __name__ == "__main__":
    root = tk.Tk()
    main_ui = gui.GUI(root)
    
    main_ui.plot_queue = queue.Queue()
    
        
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
        
    
    def plot_graph():
        try: #when queue is not empty do following
            msg = main_ui.plot_queue.get(0)
            if msg == 'plot':
                main_ui.fig_x_channel.canvas.draw()
                main_ui.fig_y_channel.canvas.draw()
                main_ui.fig_fft.canvas.draw()
            
            root.after(500, plot_graph)
            
        except queue.Empty: #when queue is empty do smth
                root.after(500, plot_graph)

    
    plot_graph()
    
    update()

    root.mainloop()
