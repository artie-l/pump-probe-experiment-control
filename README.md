# pump-probe-experiment-control 

Pump-probe experiment control is the graphical user interface (GUI) that designed to simplify, automatize, and visualize the data acquisition process.

This GUI is the "single-page" window with inputs for the time-resolved scan parameters, Lock-in Amplifier (LIA) controls, alignment tools, and plots with measured data sets. 

It was made with an intent of user-friendly software configuration, hardware initialization and modifiability of the GUI itself. No prior programming knowledge required. 

![Compiled GUI](https://i.ibb.co/bLRJ7M4/GUI.png "Compiled GUI")

## Requirements

One can copy-paste `pip` commands to install the nesessary packages. 
Python 2.7 version is chosen because of compatibility with XPS Motion controller driver. One can use the https://github.com/pyepics/newportxps repo which is compatible with Python 3+.

* python 2.7
  - https://www.python.org/ftp/python/2.7/python-2.7.amd64.msi
  - https://repo.anaconda.com/archive/Anaconda2-2019.10-Windows-x86_64.exe
    - For beginners I recommend Anaconda, as it comes with some necessary pre-installed packages, and has novice-friendly interface
* mttkinter
  - `pip install mttkinter`
* NewPort XPS motion controller driver
  - ftp://download.newport.com/MotionControl/Current/MotionControllers/XPS-Q/Drivers/python/XPS_Q8_drivers.py
* numpy
  - `pip install numpy`
* matplotlib
  - `pip install matplotlib`
* visa
  - `pip install PyVISA`
* LIA user manual
  - To know the form of queries and commands
* Access to XPS motion controller Web-Interface
  - IP, Login, Password, Delay Stage name
  
# Program setup and first launch
* Download the ZIP file and extract it to desired directory (`userdir`). 
* First one needs to check if all requirements were met. This could be done by running the `userdir/main.py` within the IDE, python console or running the `userdir/Manip Control.cmd`.  
* If you see the new window that popped-up, and it looks like the one at the top of the page, congratulations! Only communication with measurement instruments should be established!
* If you encountered an error, most likely the specific component is missing. Check the error log and see if everything from **Requirements** section is installed. 

When the GUI is displayed, one shall proceed to the establishing the connection between the LIA, Delay Line and computer running the program.

## LIA setup
We will start with the LIA. Verify if it is connected to the computer, and check that you can send and recieve the information via simple RS232 terminal (Thermite, for example https://www.compuphase.com/software_termite.htm#).

Then, navigate to `userdir/gui/` folder

## Delay line setup
