import sys
from edge import Edge
from uf import UF
from kruskal import ler_casos, kruskal


# Lógica da Segunda MST (SMST) e Integração

def segunda_mst(n, edges, mst_original_edges):
    """
    Encontra o custo da Segunda Árvore Geradora Mínima (SMST).

    Estratégia: para cada aresta pertencente à MST original, tentamos
    removê-la e rodar o Kruskal novamente. O menor custo válido obtido
    entre todas as tentativas é o custo da Segunda MST.

    Parâmetros
    ----------
    n                 : número de vértices
    edges             : lista de TODAS as arestas do grafo (já ordenada)
    mst_original_edges: lista das arestas que compõem a MST original

    Retorno
    -------
    Custo (int) da Segunda MST.
    """
    s2 = float('inf')

    for edge in mst_original_edges:
        # Tenta construir uma árvore geradora ignorando a aresta 'edge'
        s_temp, _ = kruskal(n, edges, edge_to_skip=edge)

        # Mantém o menor custo válido encontrado
        if s_temp < s2:
            s2 = s_temp

    return s2


def resolver():
    """
    Função principal: lê os casos de teste, resolve cada um e imprime
    os resultados no formato esperado pelo UVA 10600.

    Para cada caso de teste:
      1. Ordena as arestas uma única vez (otimização).
      2. Encontra S1 (MST) com Kruskal padrão.
      3. Encontra S2 (Segunda MST) por exclusão de arestas.
      4. Imprime: S1 S2
    """
    casos = ler_casos()

    for n, edges in casos:
        # Passo 1: ordenar as arestas UMA única vez (Edge implementa __lt__)
        edges.sort()

        # Passo 2: encontrar a MST original (S1)
        s1, mst_original_edges = kruskal(n, edges)

        # Passo 3: encontrar a Segunda MST (S2)
        s2 = segunda_mst(n, edges, mst_original_edges)

        # Passo 4: imprimir resultado
        print(f"{s1} {s2}")


# Ponto de entrada

if __name__ == "__main__":
    resolver()
