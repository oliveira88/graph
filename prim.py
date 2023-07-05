import math
from heapq import *
from utils import *
showTree = False

def min_spanning_tree_prim(graph: dict) -> int:
  min_spanning_tree = []
  heap = []
  visited = [False] * len(graph)
  distance = [math.inf] * len(graph)
  num_of_vertexes_in_mst = 0

  # Configuring the initial vertex
  initial_vertex = 0
  distance[initial_vertex] = 0
  visited[initial_vertex] = True
  num_of_vertexes_in_mst += 1
  for (vertex_u, cost_a) in graph[initial_vertex]:
    heappush(heap, (cost_a, initial_vertex, vertex_u)) # Pushing candidates to the heap with cost as key

  while num_of_vertexes_in_mst < len(graph):
    while True:
      cost_b, u, vertex_v = heappop(heap) # Pop the smallest cost and check if the vertex is already visited
      if not visited[vertex_v]:
        break
    
    visited[vertex_v] = True
    distance[vertex_v] = cost_b
    min_spanning_tree.append((u, vertex_v, cost_b))
    num_of_vertexes_in_mst += 1
    for (vertex_u, cost_c) in graph[vertex_v]: # Pushing new edges as candidates to the heap with cost as key
        if not visited[vertex_u]:
          heappush(heap, (cost_c, vertex_v, vertex_u))

  return min_spanning_tree, distance

graph = read_file_and_generate_graph("./txts2/arquivo1.txt")

mst, distance  = min_spanning_tree_prim(graph)
print_total_cost(distance)

if showTree:
  print(mst)