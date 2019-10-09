# Pygame 1405 Image Script

## What is this 
This program is a graphical user interface to complete the COMP 1405 first assignment. This program allows you to draw a photo using rectangles, circles, ellipses, polygons and fills. This drawing is translated into a python script which is in the assignment format. running this second python file will automatically redraw the initial image you drew and will save it to an image file. 

## Usage

after cloning the file to your computer, the gui can be booted with the command `python3 python_image_script.py`.

### Drawing

All drawing is done in the gui workspace area. rectangles, circles and ellipses are all created from click down to click up difference. fills are created by clicking anywhere on the workspace. Polygons are created by clicking in multiple places in the workspace and then clicking on the first point of the polygon to close the shape.

### Commands

Typing the following letters on the keyboard will allow you to access different functionality of the program

- `r` = draw a rectangle
- `e` = draw a ellipse 
- `c` = draw a circle
- `p` = draw a polygon
- `f` = fill the background

#### Undo

press `u` to undo the last shape drawn. Rectangles drawn during the polygon creating process are undone in this process.

### Colors
in order to change the color used in the program the arrow keys should be used. The color pallet seen in the bottom left of the screen show all colors allowed for the project. These colors will be automatically appended as comments to the next file as the assignment specifies
