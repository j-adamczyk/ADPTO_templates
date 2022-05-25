import os
from time import time

from ilp.example import solve_and_print_example
from ilp.vertex_cover import vertex_cover_solver

from utils.dimacs import *

graph_names = [
    "e5",
    "e10",
    "e20",
    "e40",
    "e150",
    "s25",
    "s50",
    "s500",
    "b20",
    "b30",
    "b100",
    "k330_a",
    "k330_b",
    "k330_c",
    "m20",
    "m30",
    "m40",
    "m50",
    "m100",
    "p20",
    "p35",
    "p60",
    "p150",
    "r30_01",
    "r30_05",
    "r50_001",
    "r50_01",
    "r50_05",
    "r100_005",
]


def calculate_vertex_cover():
    graph_dir = "graphs"
    solution_dir = "solutions"
    for name in graph_names:
        graph_filename = os.path.join(graph_dir, name)
        solution_filename = os.path.join(solution_dir, f"{name}.sol")
        G = loadGraph(graph_filename)
        G_edge_list = edgeList(G)

        print(name)
        solution = vertex_cover_solver(G)
        if not solution:
            print("solution not found")
            continue

        solution, k = solution

        print("solution k:", k)
        print("VC:", isVC(G_edge_list, solution))
        print()
        saveSolution(solution_filename, solution)
A

if __name__ == "__main__":
    # solve_and_print_example()
    calculate_vertex_cover()
    # calculate_weighted_vertex_cover()
    # calculate_approx_vertex_cover()
