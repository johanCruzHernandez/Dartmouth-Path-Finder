# Name: Johan Cruz Hernandez
# File: map_plot.py
# Date: 3.12.2021


from cs1lib import *
from load_graph import *
from bfs import *

WINDOW_WIDTH = 1012
WINDOW_HEIGHT = 811

start = None
goal = None

mouse_press = False
mouse_x = 0
mouse_y = 0

vertex_dictionary = load_graph("dartmouth_graph.txt")


# Draws the edges that connect adjacent vertices
# Parameters: receives r, g, b values for color and the
# width for the edges
def draw_edge(r, g, b, stroke_width):
    set_stroke_color(r, g, b)
    set_stroke_width(stroke_width)


# Purpose: detects if mouse is pressed ans sets boolean to True
# Parameters: receives the coordinates where the mouse was pressed
def mouse_pressed(mx, my):
    global mouse_press, mouse_x, mouse_y

    mouse_press = True

    mouse_x = mx
    mouse_y = my


# Purpose: detects of the mouse was released and sets boolean to False
# Parameters: receives x and y coordinates where mouse was released
def mouse_released(mx, my):
    global mouse_press

    mouse_press = False


# Purpose: keeps track of the x and y coordinates of the mouse
# Parameters: receives the x and y coordinates of the moue location
def mouse_moved(mx, my):
    global mouse_x, mouse_y

    mouse_x = mx
    mouse_y = my


# Main draw function that is called by start_graphics
def main():
    global start, goal

    img = load_image("dartmouth_map.png")
    draw_image(img, 0, 0)

    for v_r in vertex_dictionary:
        vertex_dictionary[v_r].draw_vertex(0, 0, 1)
        vertex_dictionary[v_r].draw_adjacent_edge(0, 0, 1)

    for v_r in vertex_dictionary:
        if mouse_press and vertex_dictionary[v_r].mouse_in_range(mouse_x, mouse_y):
            start = vertex_dictionary[v_r]
            start.draw_vertex(1, 0, 0)
        elif start is not None and not mouse_press and vertex_dictionary[v_r].mouse_in_range(mouse_x, mouse_y):
            goal = vertex_dictionary[v_r]

    path = breadth_first_search(start, goal, vertex_dictionary)
    print(path)
    # draws edges connecting adjacent vertices
    i = 0
    while i < len(path) - 1:
        draw_edge(1, 0, 0, 3)
        draw_line(path[i].x, path[i].y, path[i + 1].x, path[i + 1].y)
        i = i + 1


start_graphics(main, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, mouse_press=mouse_pressed, mouse_release=mouse_released,
               mouse_move=mouse_moved)
