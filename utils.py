import sys
from functools import reduce
from collections import defaultdict

def read_file_and_generate_graph(file_name: str) -> defaultdict:
  if len(sys.argv) > 1:
    file_name = f"./txts2/arquivo{sys.argv[1]}.txt"
  with open(file_name, "r") as file:
      [_, num_edges] = list(map(int, file.readline().split()))
      graph = defaultdict(list)
      for _ in range(num_edges):
        [u, v, weight] = list(map(int,file.readline().split()))
        graph[u].append((v, weight))
        graph[v].append((u, weight))
  return graph


def print_total_cost(distance_list: list) -> int:
  total_cost = reduce(lambda x, y: x + y, distance_list)
  print(total_cost)