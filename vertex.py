# Name: Johan Cruz Hernandez
# File: vertex.py
# Date: 3.8.2021
# Description: this file contains the class Vertex

from cs1lib import *


class Vertex:

    def __init__(self, name, x, y):
        self.name = name
        self.x = int(x)
        self.y = int(y)
        self.radius = 10
        self.adj_list = []

    def draw_vertex(self, r, g, b):

        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, self.radius)

    def draw_adjacent_edge(self, r, g, b):

        set_stroke_color(r, g, b)
        set_stroke_width(3)

        for v_adj in self.adj_list:
            draw_line(int(self.x), int(self.y), int(v_adj.x), int(v_adj.y))

    # Returns True when mouse location is on a vertex and False when mouse is not on a vertex
    def mouse_in_range(self, x, y):
        if abs(self.x - x) <= self.radius and abs(self.y - y) <= self.radius:
            return True

        return False

    def __str__(self):

        adjacent_string = ""

        for i in range(len(self.adj_list)):
            adjacent_string = adjacent_string + self.adj_list[i].name
            if i < len(self.adj_list) - 1:
                adjacent_string = adjacent_string + ", "

        return self.name + "; " + "Location: " + self.x + ", " + self.y + "; " + "Adjacent vertices: " + adjacent_string
