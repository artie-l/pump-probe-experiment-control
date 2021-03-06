# pump-probe-experiment-control 

### Navigation:
- [Requirements](#requirements)
- [Program setup and first launch](#program-setup-and-first-launch)
  * [LIA setup](#lia-setup)
  * [Delay line setup](#delay-line-setup)
- [How to launch the software](#how-to-launch-the-software)
- [Supplementary information and Troubleshooting](#supplementary-information-and-troubleshooting)
# 

# Requirements
1. Anaconda (or miniconda)
It is easy to setup the new `conda` environment with all necessary packages:
   1. One should open an Anaconda Prompt
   2. Download files from GitHub and extract them to desired directory `disk://folder/dir`
   3. Set Anaconda prompt to file directory with this command `CD disk://folder/dir`
   4. Execute `conda env create -f env_install.yml`

If it does not work, one can use the following `pip` commands to manually install the nesessary packages:

* python 3.7
  - For beginners I recommend Anaconda, as it comes with some necessary pre-installed packages, and has novice-friendly interface
* mttkinter
  - `pip install mttkinter`
* Install the NewPort XPS motion controller driver
  - https://github.com/pyepics/newportxps
* numpy
  - `pip install numpy`
* matplotlib
  - `pip install matplotlib`
* PyVISA
  - `pip install PyVISA`
* PyVISA-py
  - `pip install PyVISA-py`
* PILLOW
  - `pip install pillow`
* Pyautogui
  - `pip install pyautogui`
* LIA user manual
  - To know the form of queries and commands
* Access to XPS motion controller Web-Interface
  - IP, Login, Password, Delay Stage names
  
# Program setup and first launch
* Download the ZIP file and extract it to desired directory (`userdir/`). 
* First one needs to check if all requirements were met. This could be done by running the `userdir/main.py` within the IDE, python console or running the `userdir/Manip Control.cmd`.  
* If you see the new window that popped-up, and it looks like the one at the top of the page, congratulations! Only communication with measurement instruments should be established!
* If you encountered an error, most likely the specific component is missing. Check the error log and see if everything from **Requirements** section is installed. 

When the GUI is displayed, one shall proceed to the establishing the connection between the LIA, Delay Line and computer running the program.

## LIA setup
We will start with the LIA:

* Verify if the LIA model is **SR830**; 
  - If not, procceed to the https://github.com/artie-l/pump-probe-experiment-control/tree/master/gui/README.md and follow the instructions.
* Verify if it is connected to the computer;
* Turn ON the LIA;
* Check that you can send and recieve the information via simple RS232 terminal (Thermite, for example https://www.compuphase.com/software_termite.htm#).

Now, let's do a simple connection to LIA via Python:

1. Navigate to `userdir/gui/` folder and open `tools_initialization.py` in the IDE (Spyder, for example)
2. Run the `tools_initialization.py` file (F5 in Spyder). 
3. You should see the list of devices connected to your computer. 
4. Replace the `resource_name` (do not remove the `''` inside the parentheses) on line **126** by the full `GPIB` or `COM` address of the LIA (do not include `u`). 
   - To be sure if the adress is correct, compare it with the one found in Thermite;
5. Uncomment line **126** and **129** by removing the `# `  in front of the code (Ctrl + 1 in Spyder).
6. Re-run the script.

If the correct `IDN` of the LIA was printed in the Python console, congratulations! We are almost done with the LIA configuration. The next steps are:

1. Manually set the LIA's Sensitivity to 2V.
2. Follow the text guide (lines 131-132) in the file.
3. Uncomment lines 134 to 138.
4. Re-run the script.

* If the sensitivity was changed, and `IDN` with the number was printed in the console, LIA has been sucesfully configured. 
* If you encouner the error, try to repeat the beforementioned steps and check if `rm.list_resources` [argument](https://www.w3schools.com/python/gloss_python_function_arguments.asp) on line 49 is the same as on line 126. 

We can now proceed to the Delay Line setup.

## Delay line setup

This script supports multiple delay lines, that you can easily choose before the scan. To proceed with the setup:

* Turn on the XPS controller.
* Go to the XPS web-interface (Computer should be connected to the XPS via Ethernet cable).
* Write down the XPS web-interface url address (should be something like `192.168.0.254`)
* Log in as administrator and go to Stages or smth... To be checked.
* Write down the **full names** of the delay lines you want to use (should be something like `Group1.Pos` or `GROUP1.POSITIONER`)

Now, we can proceed with the Python part:

1. Navigate to `userdir/gui/` folder and open `gui_variables.py` in the IDE (Spyder, for example), in addition to already opened `tools_initialization.py` file.
2. Locate the `DelayLines` variable (line 35 in the `gui_variables.py` file).
3. Change its content (within the `( )`) to the **full names** of the Delay lines, enclosed in `''` and separated by coma.
    * If you are using only one delay line, the `DelayLines` variable should be defined as `DelayLines = ('full_delay_line_name', )`
4. Save and close the `gui_variables.py` file (Ctrl + S)
5. Uncomment lines 142 to 145 in `tools_initialization.py`
6. Replace `XPS_web_ip`on line 143 (do not remove the `''` inside the parentheses) by the IP address used to acess the XPS web-interface.
7. Run the code.

If you see no message printed in the console, it means that the connection to the XPS was established correctly. Now we will modify the DelayLine class:

1. Replace the `XPS_web_ip` on line 15 by the by the IP address used to acess the XPS web-interface.
2. Uncomment the lines 149 to 152.
3. Re-run the script.
4. Check in the XPS web-interface if the position of the delay-line has been changed to 25 mm.

If you have no errors, and delay line moved, congratulations. Save the `tools_initialization.py` as is and you can now use the software!

# How to launch the software

Normally, the program launch could be done in the two ways:

1. By double-clicking the `Manip Control.cmd`.
   * If this does not work, check if the python was added to the SYSTEM path. You can simply follow this [guide](https://geek-university.com/python/add-python-to-the-windows-path/).
2. By executing the `main.py` within the IDE (Spyder for example).

# What to be changed in the future
Since I am at the last year of my PhD, there is almost no time prioritize the following things. Nevertheless, following features are still in plans, and might be released in the near future:

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
or their derivatieves should be answered in the guide, or somewhat detailed explanation. It be displayed by navigationg to `gui` folder at the top of this page (or by following this link: https://github.com/artie-l/pump-probe-experiment-control/blob/master/py37/gui/README.md).

If you have any questions or suggestions, do not hesitate to contact me. 
