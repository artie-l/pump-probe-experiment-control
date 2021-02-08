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
This category contains the files that construct the GUI. If one wants to add some new functionality, one can take the one of following files as an example. If the following files are modified, the changes should be automatically included in the `gui_assembled.py`. Specific functionality (as new Graph space) might require gui assembled.py modification.
### gui scan params.py
This file creates the `Scan Parameters` section in the GUI. User should input the values that will define the time-resolved scan-window, temporal resolution and the number of scans. 
This file initializes a `Frame` that contains the `LabelFrame` with:
1. Labels to entries.
2. Entries to input the scan parameters.
###  gui filepath entries.py
This file creates the `Path and File name` section in the GUI. Here, one can set the folder to save the files to and file name. As well, it will display the current number of scan, that will be appended at the end of the filename. 
This file initializes a `Frame` that contains the `LabelFrame` with:
1. Lables to entries.
2. Entries to input the filename and path.
3. Button to choose the folder to save files to.
4. Label with the `scan_number_Var` linked to it. 
5. `get_folder_path` function, to save the path to save the data to.

The `Choose folder` button has an image linked to it, that is located in the `program_dir/misc` folder.
### gui rt lia.py
This file creates the `LIA Output, R` section in the GUI. It is used to display the live valuer of LIA's R channel with a specific delay. This LIA polling will automatically stop when the new scan is started. While the scan in process, the `Start` button remains uncative. During Quick Scan, `Start` button can be used, since no data is transfered from the LIA.
This file initializes a `Frame` that contains the `LabelFrame` with:
1. Figure to display a Graph.
2. Button to Start/Stop live LIA reading.
3. `on_off` function, that deals with Button logic.
4. `trace` function, to plot the curve.

`trace` function is called in the `main.py`, within `update` function.
### gui data graphs.py
This file creates the `Channel X` and `Complementary Info` sections in the GUI. It is used to display graphs after each scan made during data acqusition. `Channel X` section equiped with an interactive toolbar, that allows the closer inspection of the `Channel X` plot. `Complementary Info` has two tabs, `Channel Y` and `FFT`. `Channel Y` records the data from Y channel of the LIA, while `FFT` does the Fast Fourier Transform of the **average** signal displayed in the `Channel X`.
This file initializes a `Frame` that contains two `LabelFrame`'s with:
1. Frame to display the LIA's data from `Channel X`.
2. Interactive toolbar for the `Channel X` figure.
3. Frame with a Notebook that contains:
   * `Channel Y` frame, to display the LIA's data from `Channel Y`
   * `FFT` frame, to display the FFT of the data displayed in `Channel X` figure.

If one wants more plots, it is possible to follow the code. One can:
1. Create a figure in the `gui_assembled.py` (should be done before creating the graph_space).
2. Add an aditional frame.
3. Add it to an existing notebook `graph_space_Y_FFT_Notebook`.
4. Create a new canvas and draw a figure created in the Step 1, on the Frame created in the step 2
5. Place canvas on the grid
6. Draw a figure

### gui lia controls.py
This file creates the `LIA parameters` section in the GUI. It is used to change the sensitivity and time constant of the LIA. 
The file initializes a `Frame`, that contains one `LabelFrame` with:
1. Two labels.
2. Two comboboxes with Sensitivity and Time Constant values.
3. `change_tconst` function, that changes the time constant of the LIA when specific value is chosen.
3. `change_sens` function, that changes the sensitivity of the LIA when specific value is chosen.

This file imports the `LIATconstVisual` and `LIASensVisual` values from the `gui_variables.py`, in order to display them in the combobox. Normally, the LIA takes the values from 0 to n for the time constant and sensitivity. The indexes of a value in `LIATconstVisual` and `LIASensVisual` correspond to the value that one should send to LIA to set the respective time constant or sensitivity.

One can add more options in analogy with the code presented here.
### gui chopper controls.py
This file creates the `LIA parameters` section in the GUI. It is used to change the sensitivity and time constant of the LIA. 
The file initializes a `Frame`, that contains one `LabelFrame` with:
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
