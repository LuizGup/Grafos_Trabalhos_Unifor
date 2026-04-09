"""
Chinese Postman Problem - Eulerian Circuit Finder
Reads an eulerialized directed graph and finds the optimal tour.
"""

from pathlib import Path
from src.digraph import DiGraph
from src.hierholzer import DirectedEulerianCycle


def read_digraph_from_file(file_path):
    """
    Read a directed graph from file in algs4 format:
    - Line 1: number of vertices V
    - Line 2: number of edges E
    - Lines 3 to 2+E: edges in format "v w weight"
    
    Args:
        file_path: Path to input file
        
    Returns:
        DiGraph object
    """
    with file_path.open("r", encoding="utf-8") as f:
        first_line = f.readline().strip()
        second_line = f.readline().strip()

        if not first_line or not second_line:
            raise ValueError("Arquivo de entrada invalido: faltam V e E (numeros ou nao).")

        try:
            v_count = int(first_line)
            e_count = int(second_line)
        except ValueError:
            raise ValueError("V e E devem ser inteiros.")

        digraph = DiGraph(v_count)

        for i in range(e_count):
            line = f.readline().strip()
            if not line:
                raise ValueError(f"Arquivo invalido: faltando aresta na linha {i + 3}.")
            
            try:
                parts = line.split()
                if len(parts) != 3:
                    raise ValueError(f"Aresta deve ter 3 valores: v w weight.")
                v, w, weight = int(parts[0]), int(parts[1]), int(parts[2])
                digraph.add_edge(v, w, weight)
            except ValueError as e:
                raise ValueError(f"Erro na linha {i + 3}: {e}")

    return digraph


def print_balance_info(digraph):
    """Print balance information for all vertices."""
    print("Informacoes de balanceamento dos vertices:")
    all_balanced = True
    for v in range(digraph.V):
        in_deg = digraph.get_in_degree(v)
        out_deg = digraph.get_out_degree(v)
        balance = digraph.get_balance(v)
        print(f"  Vertice {v}: in-degree={in_deg}, out-degree={out_deg}, balance={balance:+d}")
        if balance != 0:
            all_balanced = False
    
    if all_balanced:
        print("✓ Todos os vertices estao balanceados (condicao para circuito euleriano)")
    else:
        print("✗ Grafo NAO pode ter circuito euleriano (vertices desbalanceados)")
    print()


def print_eulerian_circuit(hierholzer_obj):
    """Print the Eulerian circuit found."""
    if not hierholzer_obj.has_eulerian_circuit():
        print("ERRO: Nao foi encontrado circuito euleriano.")
        return

    circuit = hierholzer_obj.get_circuit()
    weight = hierholzer_obj.get_total_weight()

    print("Circuito euleriano encontrado:")
    print(" → ".join(str(v) for v in circuit))
    print(f"\nComprimento do circuito: {len(circuit) - 1} arestas")
    print(f"Peso total do circuito: {weight}")
    print()


def main():
    """Main program execution."""
    print("=" * 60)
    print("Problema do Carteiro Chines (Chinese Postman Problem)")
    print("Busca de Circuito Euleriano usando Algoritmo de Hierholzer")
    print("=" * 60)
    print()

    # Construct path to eulerialized graph file
    dados_path = Path(__file__).resolve().parent.parent / "dados" / "entrada_eulerizada.txt"

    try:
        print(f"Lendo grafo de: {dados_path}")
        digraph = read_digraph_from_file(dados_path)
        print(f"✓ Grafo lido com sucesso: {digraph.V} vertices, {digraph.E} arestas")
        print()

        # Print adjacency list
        print("Lista de adjacencia do grafo:")
        print(digraph)
        print()

        # Check balance
        print_balance_info(digraph)

        # Find Eulerian circuit
        print("Executando algoritmo de Hierholzer...")
        hierholzer = DirectedEulerianCycle(digraph)
        print()

        # Print result
        print_eulerian_circuit(hierholzer)

        print("=" * 60)

    except FileNotFoundError:
        print(f"ERRO: Arquivo nao encontrado: {dados_path}")
    except ValueError as e:
        print(f"ERRO de leitura: {e}")
    except Exception as e:
        print(f"ERRO inesperado: {e}")


if __name__ == "__main__":
    main()
