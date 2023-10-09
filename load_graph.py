# Name: Johan Cruz Hernandez
# File: load_graph.py
# Date: 3.8.2021
# Description: this file contains the load_graph code.

from vertex import Vertex


def load_graph(filename):
    vertex_dictionary = {}

    fp = open(filename)

    for l in fp:
        field_list = l.strip().split("; ")

        coordinates = field_list[2].split(", ")

        v = Vertex(field_list[0], coordinates[0], coordinates[1])

        vertex_dictionary[field_list[0]] = v

    fp.close()

    fp = open(filename)

    for l in fp:
        field_list = l.strip().split("; ")

        adj_names = field_list[1].strip().split(", ")

        current_object = vertex_dictionary[field_list[0]]

        for v_name in adj_names:
            current_object.adj_list.append(vertex_dictionary[v_name])

    fp.close()

    return vertex_dictionary


load_graph("dartmouth_graph.txt")
