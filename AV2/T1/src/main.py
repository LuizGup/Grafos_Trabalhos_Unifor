from pathlib import Path

from src.breadth_first_paths import BreadthFirstPaths
from src.depth_first_paths import DepthFirstPaths
from src.graph import Graph
from dados.dicionario import ESTADOS_NORDESTE


STATE_TO_ID = ESTADOS_NORDESTE
STATES = [state for state, _ in sorted(STATE_TO_ID.items(), key=lambda item: item[1])]


def build_graph():
	graph = Graph(len(STATES))
	indexed_edges = []

	dados_path = Path(__file__).resolve().parent.parent / "dados" / "mapa nordeste.txt"
	with dados_path.open("r", encoding="utf-8") as file:
		for raw_line in file:
			line = raw_line.strip().upper()
			if not line:
				continue

			parts = line.split()
			if len(parts) != 2:
				raise ValueError(f"Linha invalida no arquivo de arestas: '{raw_line.strip()}'")

			a, b = parts
			if a not in STATE_TO_ID or b not in STATE_TO_ID:
				raise ValueError(f"Estado invalido encontrado no arquivo de arestas: '{a} {b}'")

			v = STATE_TO_ID[a]
			w = STATE_TO_ID[b]
			indexed_edges.append((min(v, w), max(v, w)))

	indexed_edges.sort()

	for v, w in indexed_edges:
		graph.add_edge(v, w)

	return graph


def read_state(prompt):
	while True:
		state = input(prompt).strip().upper()
		if state in STATE_TO_ID:
			return state
		print("Estado invalido. Use uma sigla do Nordeste: AL, BA, CE, MA, PB, PE, PI, RN, SE.")


def format_path(path):
	if path is None:
		return "nao existe caminho"
	return " -> ".join(STATES[v] for v in path)


def main():
	graph = build_graph()

	print("Estados mapeados (ordem alfabetica):")
	print(", ".join(f"{idx}:{state}" for idx, state in enumerate(STATES)))
	print()

	origem = read_state("Informe o estado de origem (X): ")
	destino = read_state("Informe o estado de destino (Y): ")

	s = STATE_TO_ID[origem]
	t = STATE_TO_ID[destino]

	dfs = DepthFirstPaths(graph, s)
	bfs = BreadthFirstPaths(graph, s)

	alcanca = dfs.has_path_to(t)
	print("\n1) Conectividade X -> Y:")
	print(f"{origem} alcanca {destino}? {'Sim' if alcanca else 'Nao'}")

	print("\n2) Caminho encontrado por DFS:")
	print(format_path(dfs.path_to(t)))

	print("\n3) Caminho encontrado por BFS:")
	print(format_path(bfs.path_to(t)))

	print("\n4) Estados alcancaveis a partir de X:")
	alcancaveis = [STATES[i] for i, marked in enumerate(dfs.marked) if marked]
	print(", ".join(alcancaveis))

	print("\n5) Ordem de visita da DFS:")
	print(" -> ".join(STATES[v] for v in dfs.visit_order))

	print("\n6) Ordem de visita da BFS:")
	print(" -> ".join(STATES[v] for v in bfs.visit_order))


if __name__ == "__main__":
	main()
