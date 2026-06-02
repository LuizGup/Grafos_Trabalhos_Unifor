import sys
from graph import ler_entrada
from dijkstra_k import k_shortest_paths


# ──────────────────────────────────────────────────────────────
# INTEGRANTE 3 — Integração Geral e Saída
# ──────────────────────────────────────────────────────────────

def resolver():
    """
    Função principal: lê a entrada, resolve o problema e imprime
    os resultados no formato esperado pelo CSES 1196 - Flight Routes.

    Passos:
      1. Ler a entrada (grafo + parâmetros).
      2. Encontrar os k menores custos de rota com Dijkstra modificado.
      3. Imprimir os k custos separados por espaço.
    """
    # Passo 1: ler entrada (Integrante 1)
    adj, n, k = ler_entrada()

    # Passo 2: encontrar os k menores caminhos (Integrante 2)
    resultado = k_shortest_paths(adj, n, k)

    # Passo 3: imprimir resultado
    sys.stdout.write(" ".join(map(str, resultado)) + "\n")


# Ponto de entrada

if __name__ == "__main__":
    resolver()
