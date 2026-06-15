# UVa 11045 — My T-shirt suits me
### Apresentação — Grupo J

---

## 1. Contexto e objetivo (1 min)

**Problema:** Distribuir N camisetas (N/6 de cada um dos 6 tamanhos) para M voluntários.
Cada voluntário aceita exatamente 2 tamanhos. É possível atender todos?

**Objetivo:** Verificar se existe uma distribuição válida → YES ou NO.

Redução: **emparelhamento bipartido com múltiplas cópias** por tamanho,
resolvido via fluxo máximo.

---

## 2. Modelagem da rede de fluxo (1 min)

```
[Fonte S]
    │ cap = N/6 (por tamanho)
    ▼
[XXL] [XL] [L] [M] [S] [XS]   ← 6 nós de tamanho
    │ cap = 1 (se o voluntário aceita)
    ▼
[V1] [V2] ... [VM]             ← M nós de voluntário
    │ cap = 1
    ▼
[Sorvedouro T]
```

- **Fonte → tamanho:** limita o estoque (N/6 unidades)
- **Tamanho → voluntário:** existe aresta se o voluntário aceita aquele tamanho
- **Voluntário → sorvedouro:** garante que cada um recebe no máximo 1 camiseta

---

## 3. Algoritmo e grafo residual (1 min)

**Algoritmo escolhido:** Ford-Fulkerson com DFS

- Enquanto existir caminho S → T com capacidade residual > 0:
  1. Encontra o caminho via DFS
  2. Calcula o gargalo (menor capacidade residual do caminho)
  3. Envia o gargalo pelo caminho
  4. Atualiza o grafo residual (diminui direto, aumenta reverso)

**Grafo residual:** arestas reversas permitem "desfazer" alocações.
Se V2 tomou o tamanho L mas V3 precisa de L exclusivamente, o algoritmo
redireciona via aresta reversa.

**Condição de parada:** nenhum caminho S → T no grafo residual.

---

## 4. Conversão do fluxo na resposta (1 min)

- Cada unidade de fluxo = 1 voluntário recebendo 1 camiseta
- Se fluxo máximo == M → **YES** (todos atendidos)
- Se fluxo máximo < M → **NO** (estoque insuficiente de algum tamanho)

Não é necessário reconstruir a alocação — apenas o valor do fluxo basta.

---

## 5. Complexidade e casos especiais (1 min)

**Complexidade:**
- Vértices: 2 + 6 + M ≤ 38
- Arestas: 6 + 2M + M ≤ 96
- Ford-Fulkerson DFS: O(E · f*) = O(96 × 30) ≈ **2.880 operações por caso**

**Por que não Edmonds-Karp?**
Com f* ≤ 30 e grafo minúsculo, Ford-Fulkerson DFS é mais simples e igualmente eficiente.
Edmonds-Karp (BFS) seria O(V · E²) ≈ 350.000 — desnecessário aqui.

**Casos especiais:**
- N > M não garante YES se um tamanho específico está sobrecarregado
- Se todos os voluntários aceitam apenas os mesmos 2 tamanhos e M > 2·(N/6) → NO
- N = M: sem folga, cada camiseta deve ser usada com precisão
