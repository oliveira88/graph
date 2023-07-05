import sys
from collections import defaultdict
import math
import heapq

def min_spanning_tree_prim(graph: dict) -> int:
  vertexes_in_spanning_tree = []
  spanning_tree = []
  current_vertex = 0
  vertexes_in_spanning_tree.append(current_vertex)
  total_cost = 0
  while (len(vertexes_in_spanning_tree) - 1) != len(graph):
    minor_edge = math.inf
    for vertex in vertexes_in_spanning_tree:
      graph[vertex]
    for edge in graph[vertex]:
      if edge[0] not in vertexes_in_spanning_tree and edge[1] < minor_edge[1]:
        minor_edge = edge
      print(f"graph[{current_vertex}]: {edge}")
    print("")
    spanning_tree.append((current_vertex, minor_edge[0]))
    current_vertex = minor_edge[0]
    vertexes_in_spanning_tree.append(current_vertex)

def read_file_and_generate_graph(file_name: str) -> list:
  if len(sys.argv) > 1:
    file_name = f"./txts2/arquivo{sys.argv[1]}.txt"
  with open(file_name, "r") as file:
      [num_vertices, num_edges] = list(map(int, file.readline().split()))
      graph = defaultdict(list)
      for _ in range(num_edges):
        [u, v, weight] = list(map(int,file.readline().split()))
        graph[u].append((v, weight))
        # print(f"graph[{u}].append({v, weight})")
        # graph[v].append((u, weight))
  return num_vertices, num_edges, graph


vertices, _, graph = read_file_and_generate_graph("./txts2/arquivo1.txt")
# totalweight = min_spanning_tree_prim(graph)


  

