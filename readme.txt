The libraries being imported to run the code are:
1. import numpy as np
2. import math
3. import pygame
4. from sys import exit


To run the codes:
1. Navigate to the terminal of the saved folder.
2. Then enter:
   - "python3 Dijkstra_point.py"
   - "python3 Dijkstra_rigid.py"
   - "python3 Astar_point.py"
   - "python3 Astar_rigid.py" 
3. Enter the required inputs


The inputs for Dijkstra Point:
 -Start node, End node and resolution.

The inputs for Dijkstra Rigid:
 -Start node, End node, Resolution, Radius and Clearance.

The inputs for A* Point:
 -Start node, End node and resolution.

The inputs for A* Rigid:
 -Start node, End node, Resolution, Radius and Clearance.

The inputs:
Start Node and End Node: 
- Should be outside Obstacle space
- Should be inside Workspace
- Should be integer value
if given, an error is thrown for each.

Resolution, Radius and Clearance have to be integers.

The animation will automatically close after 15 seconds
The approximate time for Dijkstra is 1 minute and 30 seconds.
The approximate time for A star is 45 seconds.

All the inputs have to be numbers; not letters, symbols or blank input.


