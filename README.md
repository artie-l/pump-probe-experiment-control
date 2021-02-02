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
* PyVISA
  - `pip install PyVISA`
* PyVISA-py
  - `pip install PyVISA-py`
* LIA user manual
  - To know the form of queries and commands
* Access to XPS motion controller Web-Interface
  - IP, Login, Password, Delay Stage name
  
# Program setup and first launch
* Download the ZIP file and extract it to desired directory (`userdir/`). 
* First one needs to check if all requirements were met. This could be done by running the `userdir/main.py` within the IDE, python console or running the `userdir/Manip Control.cmd`.  
* If you see the new window that popped-up, and it looks like the one at the top of the page, congratulations! Only communication with measurement instruments should be established!
* If you encountered an error, most likely the specific component is missing. Check the error log and see if everything from **Requirements** section is installed. 

When the GUI is displayed, one shall proceed to the establishing the connection between the LIA, Delay Line and computer running the program.

## LIA setup
We will start with the LIA:

* Verify if the LIA model is **SR830**; 
  - If not, procceed to the https://github.com/artie-l/pump-probe-experiment-control/tree/master/gui and follow the instructions there.
* Verify if it is connected to the computer;
* Turn ON the LIA;
* Check that you can send and recieve the information via simple RS232 terminal (Thermite, for example https://www.compuphase.com/software_termite.htm#).

Now, let's do a simple connection to LIA via Python:

1. Navigate to `userdir/gui/` folder and open `tools_initialization.py` in the IDE (Spyder, for example)
2. Run the `tools_initialization.py` file (F5 in Spyder). 
3. You should see the list of devices connected to your computer. 
4. Copy and paste the full `GPIB` or `COM` adress of the LIA to the line **122**, right between the `''` (To be sure, compare it with the one seen in Thermite).
5. Uncomment line **122** and **125** by removing the `# ` in front of the code.
6. Re-run the script.

If the correct `IDN` of the LIA was printed in the Python console, congratulations! We are almost done with the LIA setup. To finish the setup:

1. Manually set the LIA's Sensitivity to 2V.
2. Follow the text guide in the file
3. Uncomment lines 130 to 133 inclusive.
4. Re-run the script.

If the sensitivity was changed, 
## Delay line setup
