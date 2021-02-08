# Supplementary information and Troubleshooting

![Program layout](https://i.ibb.co/QX3QTdj/program-structure.png "Program Layout")

## Navigation:
- [Program structure](#program-structure)
  * [main.py](#mainpy)
  * [gui Folder](#gui-folder)
    * [gui assembled.py](#gui-assembledpy)
    * [GUI elements category](#gui-elements-category)
      + [gui scan params.py](#gui-scan-paramspy)
      + [gui filepath entries.py](#gui-filepath-entriespy)
      + [gui rt lia.py](#gui-rt-liapy)
      + [gui data graphs.py](#gui-data-graphspy)
      + [gui lia controls.py](#gui-lia-controlspy)
      + [gui chopper controls.py](#gui-chopper-controlspy)
      + [gui delay line controls.py](#gui-delay-line-controlspy)
      + [gui scan controls.py](#gui-scan-controlspy)
  * [GUI logic category](#gui-logic-category)
    + [gui logic.py](#gui-logicpy)
  * [Hardware category](#hardware-category)
    + [tools initialization.py](#tools-initializationpy)
  * [Uncategorized files](#uncategorized-files)
    + [measurement functions.py](#measurement-functionspy)
    + [gui variables.py](#gui-variablespy)
    
# 

# Program structure
Here is the quick description of each file that the program is built of. It can be used as the reference for further modification or upgrade. Programm visual structure is shown in the figure above.
## main.py
`main.py` should be used to launch the program. It compiles the GUI, and is responsible for the the real-time LIA reading, in the `LIA Output,R` via the function `update`. 

If one wants to launch the program without opening an IDE, one should run the `main.py` via command prompt as `python main.py`.  Note, that command promt should be set to the directory where `main.py` is located. To do this, one can use the `Manip Control.cmd` which is included in the repo.
# gui Folder
All the following files are located in the `program_dir/gui`. The location of those should remain unchanged for the programm to function. Do not create the files in the `root` python or Spyder directory, as it might cause interference. 
## gui assembled.py
This file is used to combine 3 core modules together: GUI elements, GUI logic and Hardware. What it does:
1. It creates the programm window and adds all the components
2. It creates the Figures and toolbar through matplotlib. 
3. It has some specific elements like Proggressbars and Initialize button elements. 
4. When the initialize button is pressed, it will check the connection to the instruments (LIA and Delay Lines), and will give the respective error is the connection can not be establised.

If one wants to add a new element to the GUI, it should be initialized within the `gui_assembled.py`, to appear in the program.

## GUI elements category
This category contains the files that construct the GUI. If one wants to add some new functionality, one can take the one of following files as an example. 
### gui scan params.py
This file creates the `Scan Parameters` section in the GUI. User should input the values that will define the time-resolved scan-window, temporal resolution and the number of scans. 
This file initializes a `Frame` that contains the `LabelFrame` with:
1. Labels to entries.
2. Entries to input the scan parameters.
###  gui filepath entries.py
This file creates the `Path and File name` section in the GUI. Here, one can set the folder to save the files to and file name. As well, it will display the current number of scan, that will be appended at the end of the filename. 
This file initializes a `Frame` that contains the `LabelFrame` with:
1. Labels to entries.
2. Entries to input the scan parameters.
### gui rt lia.py
text
### gui data graphs.py
text
### gui lia controls.py
text
### gui chopper controls.py
text
### gui delay line controls.py
text
### gui scan controls.py
text
## GUI logic category
text
### gui logic.py
text
## Hardware category
text
### tools initialization.py
text
## Uncategorized files
text
### measurement functions.py
text
### gui variables.py
text
