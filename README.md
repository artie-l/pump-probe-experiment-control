# pump-probe-experiment-control 

Pump-probe experiment control is the graphical user interface (GUI) that designed to simplify, automatize, and visualize the data acquisition process.

This GUI is the "single-page" window with inputs for the time-resolved scan parameters, Lock-in Amplifier (LIA) controls, alignment tools, and plots with measured data sets. 

It was made with an intent of user-friendly software configuration, hardware initialization and modifiability of the GUI itself. No prior programming knowledge required. 

<figure><img src="https://i.ibb.co/bLRJ7M4/GUI.png" alt="GUI" border="0"><figcaption>Graphical User Interface</figcaption></figure>

## Requirements

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
* will be completed later

* LIA user manual

# Setting-up the program

First one needs to check if all requirements were met. This could be done by running the `path/main.py` within the IDE or python console.  
If you see the new window that popped-up, and it looks like @fig:description. At this point, user should configure the LIA and Delay Line. The necessary steps are explained in the respective sections. 

## LIA setup

## Delay line setup
