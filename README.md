# Dartmouth Path Finder
## Author: Johan Cruz Hernandez
## Programming Language: Python
### About
This program uses the breadth-first search algorithm to display the shortest path between two points (modeled as vertices) on the Dartmouth College campus.
### How to run:
To run this program, simply download the repository and run the map_plot.py program.
### How to use:
This program is super simple to use.
- To start: click on one vertex labeled as a blue dot.
- Then, hover your mouse over a second vertex. 
- To select a new reference (start) node, click on a blue vertex.
### Files
- map_plot.py: draws vertices on map and makes a call to the breadth-first-search algorithm to display the shortest path between two vertices
- load_graph.py: reads dartmouth_graph.txt and builds vertices.txt
- vertex.py: vertex class to represent a node
- vertices.txt: stores the vertices of an adjacent vertex in csv format and also the location on the darmtouth_graph.png
- dartmouth_graph.txt: stores a location (and its coordinates) on the campous as well as the adjacent locations
- dartmouth_map.png: map of dartmouth campus
