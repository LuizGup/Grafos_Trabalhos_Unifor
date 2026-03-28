from collections import deque
from pathlib import Path

from src.cc import CC
from src.cycle import Cycle
from src.graph import Graph


def read_graph_from_file(file_path):
	with file_path.open("r", encoding="utf-8") as f:
		first = f.readline().strip()
		second = f.readline().strip()

		if not first or not second:
			raise ValueError("Arquivo de entrada invalido: faltam V e E.")

		v_count = int(first)
		e_count = int(second)
		graph = Graph(v_count)

		for i in range(e_count):
			line = f.readline().strip()
			if not line:
				raise ValueError(f"Arquivo invalido: faltando aresta na linha {i + 3}.")
			v, w = line.split()
			graph.add_edge(v, w)

	return graph


def print_adjacency_list(graph):
	print("Lista de adjacencia do grafo do cavalo (3x3):")
	for v in range(graph.V):
		neighbors = " ".join(str(w) for w in graph.adj[v])
		print(f"{v}: {neighbors}")


def print_connected_components(graph):
	cc = CC(graph)
	print(f"\nComponentes conexas: {cc.count}")

	components = [[] for _ in range(cc.count)]
	for v in range(graph.V):
		components[cc.id[v]].append(v)

	for idx, vertices in enumerate(components):
		vertices.sort()
		vertices_text = " ".join(str(v) for v in vertices)
		print(f"Vertices da componente {idx}: {vertices_text}")


def shortest_distance(graph, source, target):
	marked = [False for _ in range(graph.V)]
	dist_to = [-1 for _ in range(graph.V)]

	marked[source] = True
	dist_to[source] = 0
	queue = deque([source])

	while queue:
		v = queue.popleft()
		if v == target:
			return dist_to[v]

		for w in graph.adj[v]:
			if not marked[w]:
				marked[w] = True
				dist_to[w] = dist_to[v] + 1
				queue.append(w)

	return -1


def print_distance_analysis(graph):
	source = 0  # (0,0)
	target = 8  # (2,2)
	distance = shortest_distance(graph, source, target)

	print("\nDistancia minima entre (0,0) e (2,2):")
	if distance == -1:
		print("Nao existe caminho entre os vertices 0 e 8.")
	else:
		print(f"{distance} movimento(s)")


def print_cycle_analysis(graph):
	cycle = Cycle(graph)

	print("\nO grafo possui ciclo?")
	print("Sim" if cycle.has_cycle else "Nao")

	print("\nAnalise de complexidade (algoritmo DFS para ciclo):")
	print("Tempo: O(V + E)")
	print("Espaco: O(V)")

	if cycle.has_cycle:
		cycle_text = " ".join(str(v) for v in cycle.cycle)
		print("\nUm ciclo encontrado:")
		print(cycle_text)


def main():
	input_path = Path(__file__).resolve().parent.parent / "dados" / "entrada.txt"
	graph = read_graph_from_file(input_path)

	print_adjacency_list(graph)
	print_connected_components(graph)
	print_distance_analysis(graph)
	print_cycle_analysis(graph)


if __name__ == "__main__":
	main()
