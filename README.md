# pump-probe-experiment-control 

### Navigation:
- [Features](#features)
- [How to launch the programm](#how-to-launch-the-programm)
- [What to be changed in the future](#what-to-be-changed-in-the-future)
- [Supplementary information and Troubleshooting](#supplementary-information-and-troubleshooting)
# 

Pump-probe experiment control is the graphical user interface (GUI) that designed to simplify, automatize, and visualize the data acquisition process.

This GUI is the "single-page" window with inputs for the time-resolved scan parameters, Lock-in Amplifier (LIA) controls, alignment tools, and plots with measured data sets. 

It was made with an intent of user-friendly software configuration, hardware initialization and modifiability of the GUI itself. No prior programming knowledge required. 

![Compiled GUI](https://i.ibb.co/bLRJ7M4/GUI.png "Compiled GUI")

# Features

1. **Easy control over the scan parameters**:
   * Initial and final positions
   * Time step
   * Number of scans, for averaging
   * Supports backward and forward scanning (Init pos < Final pos & Step > 0 or Init pos > Final pos & Step < 0)
2. **Auto-lookup for the maxima or the minima of the signal**:
   * After the acqusition is finished, reposition the Delay line at the maxima or minima of the signal by the press of the button!
3. **Delay line positioning and speed control**:
   * Move delay line to the specific position or change it's speed within the GUI.
4. **Adjustment of the LIA time constant and sensitivity**.
5. **Save the data to the specific folder with a specific filename**.
6. **Tracking of the amount of data accumulated during the day**:
   * Scan index will be appended at the end of the filename.
   * If program will be closed, the scan index will be saved, no data will be overwritten!
7. **Real-time LIA display for the signal's amplitude optimization**:
   * Make a scan, go to Max and optimize!
8. **Scan Pause and Stop functionality**:
   * Pause will pause acquisition after the current scan is finished
   * Stop will wait for the end of the current scan and stop acquisition
9. **Quick Scan functionallity**:
   * Quick Scan will not save any data.
   * Can work with Real-time LIA display.
   * It will move the delay line within the defined time-frames (Scan Parameters), so one easilly optimize the amplitude of the signal
10. **Graphs, that are updated after each scan**:
    * Data recorded from X channel, plotted in function of Time delay and Delay Line position.
    * Interactive toolbar for the X channel plot.
    * Data recorded from Y channel, plotted in function of Time delay and Delay Line position.
    * FFT of Data recorded from X channel, plotted in function Frequency (THz).
11. **Save the Graphs and data**:
    * Create the All scans file, that will be updated after each scan made (LIA readings in Volts vs Time delay)
    * Save the X and Y channel plot(Average + last scan on the same plot), after acqusition is terminated or stopped.
    * Save the Mean scans fille (average of X or Y channel data) (LIA readings in Volts vs Time delay).
12. **Auto save and recall the parameters**:
    * The programm will save all the values (Scan folder, File name, Scan parameters, LIA sensitivity and time constant)
    * Upon the Initialization of the programm, all values will be restored and automatically filled in the respective entries.
13. **Take a screenshot**:
    * Save the printscreen, to capture the values of all input parameters.
14. **Multiple Delay Line support**:
    * Select or change the stage to be used for the next measurement.
14. **Chopper frequency control** (disabled by the default):
    * Set a mechanical chopper, connected to LIA, to modulate the signal at a specific frequency (see [supplementary infromation](https://github.com/artie-l/pump-probe-experiment-control/blob/master/gui/README.md#gui-chopper-controlspy)).

# How to launch the programm
1. Old version that works **only** with python 2.7. Guide can be found [here](https://github.com/artie-l/pump-probe-experiment-control/tree/master/py27)
2. Added version that works with python 3.7. Guide can be found [here](https://github.com/artie-l/pump-probe-experiment-control/tree/master/py37)

# What to be changed in the future
Since I am close to the PhD defense, there is almost no time for the further program developement and polishing. Nevertheless, following features are still in plans, and might be released in the near future:

1. First-launch setup window, to configure the LIA and DelayLines, in order not to mess with the .py files.
2. The Windows/Linux installer.

# Supplementary information and Troubleshooting
This section should be reffered to if one has some problems with the software, wants to add/modify some GUI elements. 
The following questions:
1. How to make it work with different LIA? ;
2. What is the measurement routine? ;
3. What this button does? ;
4. Where I can find this element of the GUI?;
5. Etc.,

These questions and their derivatives are adressed/explained in the following guide, which is avialiable here: https://github.com/artie-l/pump-probe-experiment-control/blob/master/py27/gui/README.md.

If you have any questions or suggestions, do not hesitate to contact me. 
