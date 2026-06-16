# UVa 11045 — My T-shirt suits me

## Link do Problema
https://onlinejudge.org/external/110/11045.pdf

## Link do Vídeo
https://youtu.be/XZg3VD1M84g

## Integrantes do Grupo
- João Isaías — 2310283
- Luiz Carlos — 2410410
- Ricardo André — 2417200

## Linguagem Utilizada
Python 3

## Como Executar
```bash
python3 src/main.py < dados/entradas_do_problema.txt
```
Todos os arquivos de `src/` devem estar na mesma pasta ao executar.

---

## Modelagem como Rede de Fluxo

O problema é um **emparelhamento bipartido com múltiplas cópias** por tamanho,
resolvido como fluxo máximo em rede capacitada.

### Vértices
| Vértice | Descrição |
|---|---|
| 0 — Fonte (S) | Representa o estoque total de camisetas |
| 1 a 6 | Um nó por tamanho: XXL=1, XL=2, L=3, M=4, S=5, XS=6 |
| 7 até 7+M-1 | Um nó por voluntário |
| 7+M — Sorvedouro (T) | Representa a conclusão de todas as alocações |

### Arestas e Capacidades
| Aresta | Capacidade | Significado |
|---|---|---|
| Fonte → tamanho_i | N/6 | Estoque disponível de cada tamanho |
| tamanho_i → voluntário_j | 1 | Voluntário j aceita o tamanho i |
| voluntário_j → Sorvedouro | 1 | Cada voluntário recebe no máximo 1 camiseta |

---

## Algoritmo Utilizado
**Ford-Fulkerson com DFS** (busca em profundidade para caminhos aumentantes).

As classes `FlowEdge`, `FlowNetwork` e `FordFulkerson` foram implementadas
do zero seguindo a estrutura do algs4 (Sedgewick & Wayne, 4ª edição).

---

## Papel do Grafo Residual

O grafo residual mantém, para cada aresta, a capacidade ainda disponível.
Arestas reversas permitem "desfazer" alocações anteriores: se um tamanho foi
atribuído a um voluntário mas outro voluntário precisaria dele com exclusividade,
o algoritmo pode redirecionar o fluxo pela aresta reversa.

---

## Como o Fluxo é Convertido na Resposta

Cada unidade de fluxo que chega ao sorvedouro representa um voluntário que
recebeu uma camiseta que lhe serve. Se o fluxo máximo for igual a M, todos
foram atendidos (YES). Caso contrário (NO).

---

## Emparelhamento Bipartido

Não há corte mínimo nem reconstrução de caminhos neste problema.
O resultado é obtido diretamente pelo valor do fluxo máximo comparado a M.
O emparelhamento bipartido está implícito: tamanhos de um lado, voluntários
do outro, com capacidade N/6 na fonte controlando o estoque por tamanho.

---

## Análise de Complexidade

- Vértices: 2 + 6 + M ≤ 38
- Arestas: 6 + 2·M + M = 6 + 3·M ≤ 96
- Ford-Fulkerson DFS: **O(E · f\*)** onde f* ≤ M ≤ 30
- Por caso de teste: O(96 × 30) = **O(2.880)** — constante na prática

Escolhemos Ford-Fulkerson com DFS em vez de Edmonds-Karp porque o fluxo
máximo f* é pequeno (≤ 30). O(E · f*) é mais simples e eficiente aqui do
que O(V · E²) do Edmonds-Karp.

---

## Casos Especiais Relevantes

- **N > M com concentração de tamanhos:** sobram camisetas, mas se mais de
  N/6 voluntários precisam do mesmo tamanho, é NO.
- **Todos aceitam os mesmos 2 tamanhos:** se M > 2·(N/6), é NO.
- **N = M:** sem folga — cada camiseta deve ser alocada com precisão.
- **Voluntário com 2 tamanhos iguais:** não ocorre segundo o enunciado, mas
  a modelagem suportaria sem problemas.

---

## Evidência de Accepted
<!-- Adicione aqui o print ou link após submeter no UVa Online Judge -->
`evidencias/accepted.png`
