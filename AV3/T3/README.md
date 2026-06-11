# UVA 11045 – My T-shirt suits me

## Descrição do Problema

Victor é instrutor de um programa ambiental voluntário e precisa distribuir **N camisetas**
para **M voluntários**, sendo que:

- N é múltiplo de 6 e N ≥ M
- Há exatamente **N/6 camisetas de cada tamanho**: XXL, XL, L, M, S e XS
- Cada voluntário aceita **exatamente dois tamanhos**
- Cada voluntário recebe **no máximo uma camiseta**

O objetivo é determinar se é possível distribuir as camisetas de forma que
**todos os voluntários recebam uma camiseta que lhes sirva**.

**Restrições:**
- `1 ≤ N ≤ 36` (múltiplo de 6)
- `1 ≤ M ≤ 30`
- `N ≥ M`

---

## Estrutura do Repositório

```
T3/
├── main.py                       # Ponto de entrada: lê stdin, imprime YES/NO
├── README.md                     # Este arquivo
├── T3.md                         # Enunciado do trabalho
├── apresentacao/                 # Slides da apresentação
├── cses/                         # (não aplicável a este problema)
├── dados/                        # Arquivos de entrada para teste
│   └── input.txt                 # Exemplo de entrada
├── evidencias/                   # Print do Accepted no UVA Online Judge
└── src/
    ├── __init__.py
    ├── flow_edge.py              # Aresta de fluxo com capacidade e fluxo atual
    ├── flow_network.py           # Rede de fluxo com listas de adjacência
    ├── breadth_first_paths.py    # BFS no grafo residual (caminho aumentante)
    ├── ford_fulkerson.py         # Algoritmo Ford-Fulkerson com BFS
    └── tshirt_network.py         # Constrói a rede específica do problema
```

---

## Como Executar

### Pré-requisitos

- Python 3.6 ou superior
- Nenhuma biblioteca externa necessária

### Passo a passo

**1. Clone o repositório:**
```bash
git clone https://github.com/<seu-usuario>/Grafos_Trabalhos_Unifor.git
cd Grafos_Trabalhos_Unifor/AV3/T3
```

**2. Crie um arquivo de entrada** (ou use o que está em `dados/input.txt`):
```
3
18 6
L XL
XL L
XXL XL
S XS
M S
M L
6 4
S XL
L S
L XL
L XL
6 1
L M
```

**3. Execute:**

No Windows (CMD):
```cmd
python src\main.py < dados\input.txt
```

No Linux/Mac:
```bash
python3 src/main.py < dados/input.txt
```

### Saída esperada

```
YES
NO
YES
```

### Explicação dos casos

**Caso 1 (YES):** 18 camisetas → 3 de cada tamanho. Os 6 voluntários têm
preferências variadas e é possível distribuir sem conflito.

**Caso 2 (NO):** 6 camisetas → 1 de cada tamanho. 3 dos 4 voluntários querem
tamanho L, mas só há 1 disponível. Fluxo máximo = 3 ≠ 4.

**Caso 3 (YES):** 6 camisetas → 1 de cada tamanho. 1 voluntário quer L ou M.
Qualquer um dos dois serve. Fluxo máximo = 1 = M.

---

## Modelagem como Rede de Fluxo

O problema é reduzido a um problema de **fluxo máximo em rede bipartida**.

### Intuição

Imagine que as camisetas são "água" fluindo por canos:
- A **fonte** representa o estoque total
- Os **tamanhos** são depósitos intermediários, cada um com capacidade N/6
- Os **voluntários** só podem receber água de tamanhos compatíveis
- O **sorvedouro** absorve o fluxo — cada voluntário entrega 1 unidade

Se o fluxo máximo for igual a M → **YES**. Caso contrário → **NO**.

### Estrutura da Rede

```
fonte (s)
   ├──[cap = N/6]──► [XXL] ──[cap=1]──► voluntários que aceitam XXL ──[cap=1]──► sorvedouro (t)
   ├──[cap = N/6]──► [XL]  ──[cap=1]──► voluntários que aceitam XL  ──[cap=1]──► sorvedouro (t)
   ├──[cap = N/6]──► [L]   ──[cap=1]──► voluntários que aceitam L   ──[cap=1]──► sorvedouro (t)
   ├──[cap = N/6]──► [M]   ──[cap=1]──► voluntários que aceitam M   ──[cap=1]──► sorvedouro (t)
   ├──[cap = N/6]──► [S]   ──[cap=1]──► voluntários que aceitam S   ──[cap=1]──► sorvedouro (t)
   └──[cap = N/6]──► [XS]  ──[cap=1]──► voluntários que aceitam XS  ──[cap=1]──► sorvedouro (t)
```

### Numeração dos Nós

| Nó | Representa |
|----|-----------|
| `0` | Fonte (source) |
| `1` | Tamanho XXL |
| `2` | Tamanho XL |
| `3` | Tamanho L |
| `4` | Tamanho M |
| `5` | Tamanho S |
| `6` | Tamanho XS |
| `7` até `7+M-1` | Voluntários (0 a M-1) |
| `7+M` | Sorvedouro (sink) |

### Arestas e Capacidades

| Aresta | Capacidade | Justificativa |
|--------|-----------|---------------|
| Fonte → Tamanho[i] | `N/6` | Cada tamanho tem exatamente N/6 unidades disponíveis |
| Tamanho[i] → Voluntário[j] | `1` | O voluntário pode receber no máximo 1 camiseta daquele tamanho |
| Voluntário[j] → Sorvedouro | `1` | Cada voluntário recebe no máximo 1 camiseta no total |

---

## Algoritmo: Ford-Fulkerson com BFS (Edmonds-Karp)

### Como funciona

O algoritmo executa os seguintes passos repetidamente:

1. **BFS** no grafo residual para encontrar um caminho aumentante de `s` até `t`
2. **Gargalo**: calcula a menor capacidade residual ao longo do caminho
3. **Atualização**: envia fluxo igual ao gargalo, atualizando as capacidades residuais
4. **Para** quando não existir mais caminho de `s` a `t` no grafo residual

### Grafo Residual

Cada aresta `u → v` com capacidade `c` e fluxo `f` gera:
- Aresta direta `u → v` com capacidade residual `c - f`
- Aresta reversa `v → u` com capacidade residual `f`

A aresta reversa permite que o algoritmo "desfaça" decisões anteriores,
garantindo que a solução ótima seja encontrada.

### Por que BFS e não DFS?

| Critério | Ford-Fulkerson (DFS) | Edmonds-Karp (BFS) |
|----------|---------------------|-------------------|
| Busca de caminho | Qualquer caminho | Menor número de arestas |
| Número de iterações | O(valor do fluxo) | O(V · E) |
| Risco de lentidão | Sim, com capacidades grandes | Não |
| Terminação | Garantida só com inteiros | Sempre garantida |

Optamos por **Edmonds-Karp (BFS)** porque garante terminação previsível e
a classe `BreadthFirstPaths` já faz parte da base `algs4-py` do curso.

### Complexidade

- **Tempo:** `O(V · E²)` — Edmonds-Karp
- **Memória:** `O(V + E)` — listas de adjacência com arestas residuais
- Para este problema: `V ≤ 38`, `E ≤ 96` → execução instantânea

---

## Referência à Base algs4-py

| Classe | Inspirada em | Convenções mantidas |
|--------|-------------|---------------------|
| `FlowEdge` | `Edge` + `DirectedEdge` | atributos `v`, `w`; métodos `From()`, `To()`, `other()` |
| `FlowNetwork` | `Graph` | atributos `V`, `E`, `adj`; métodos `add_edge()`, `__str__()` |
| `BreadthFirstPaths` | `BreadthFirstPaths` | atributos `_marked`, `edge_to`; métodos `_bfs()`, `has_path_to()`, `path_to()` |
| `FordFulkerson` | — | orquestra `BreadthFirstPaths` e `FlowNetwork` |

---

## Dependências

Nenhuma biblioteca externa. Apenas módulos da biblioteca padrão do Python 3:
- `sys` — leitura eficiente da entrada via `stdin`
- `collections.deque` — fila para BFS
