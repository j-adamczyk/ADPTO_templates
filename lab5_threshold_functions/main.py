import os

from lab5_threshold_functions.sat.types import EdgeList, VertexSets
from sat.vertex_cover_threshold import solve_vertex_cover_threshold
from sat.vertex_cover_sortnet import solve_vertex_cover_sortnet
from utils.dimacs import *

# commented out the hardest graphs, since they take LONG time to calculate
graph_names = [
    "e5",
    "e10",
    "e20",
    "e40",
    # "e150",
    "s25",
    "s50",
    "s500",
    "b20",
    # "b30",
    # "b100",
    # "k330_a",
    # "k330_b",
    # "k330_c",
    # "k330_d",
    # "k330_e",
    # "k330_f",
    # "f30",
    # "f35",
    # "f40",
    # "f56",
    "m20",
    "m30",
    "m40",
    "m50",
    # "m100",
    "p20",
    "p35",
    "p60",
    # "p150",
    # "p200",
    "r30_01",
    "r30_05",
    "r50_001",
    "r50_01",
    # "r50_05",
    # "r100_005",
    # "r100_01",
    # "r200_001",
    # "r200_005"
]


x3c_names = [
    "10.no.x3c",
    "10.yes.x3c",
    "50.no.x3c",
    "50.yes.x3c",
    "100.no.x3c",
    "200.no.x3c",
    "200.yes.x3c",
    "350.no.x3c",
    "350.yes.x3c",
    "500.no.x3c",
    "500.yes.x3c",
    "600.no.x3c",
    "600.yes.x3c",
]


if __name__ == "__main__":
    graph_dir = "graphs"
    solution_dir = "graphs_solutions"
    for name in graph_names:
        graph_filename = os.path.join(graph_dir, name)
        solution_filename = os.path.join(solution_dir, f"{name}.sol")

        G: VertexSets = loadGraph(graph_filename)
        G_edge_list: EdgeList = edgeList(G)

        print(name)
        for k in range(1, len(G)):
            solution = solve_vertex_cover_threshold(G, k)
            if not solution or not isVC(G_edge_list, solution):
                continue

            print("solution k:", k)
            print("VC:", isVC(G_edge_list, solution), "\n")
            print()
            saveSolution(solution_filename, solution)
            break
