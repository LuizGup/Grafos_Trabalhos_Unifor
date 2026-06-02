# Checklist para Nota 10 — T2 (CSES Flight Routes)

> Documento temporário de acompanhamento. Atualizar conforme cada item for concluído.
> **Última atualização:** 2026-06-02

---

## 🟢 Código-Fonte (Pronto)

- [x] `src/directed_edge.py` — Classe DirectedEdge (baseada no algs4)
- [x] `src/graph.py` — Lista de adjacência + parser de entrada
- [x] `src/dijkstra_k.py` — Dijkstra modificado para k menores caminhos
- [x] `src/main.py` — Integração, leitura → algoritmo → saída
- [x] `dados/entradas_do_problema.txt` — Sample input do CSES
- [x] Saída correta no teste local (`4 4 7` ✅)

---

## 🔴 Submissão e Repositório (vale 1,0 pt)

### Accepted no CSES (0,50 pts)
- [ ] Criar conta no CSES (https://cses.fi/)
- [ ] Submeter solução em https://cses.fi/problemset/task/1196
- [ ] Obter status **Accepted**
- [ ] Capturar screenshot → `evidencias/accepted.png`

### Organização do repositório (0,25 pts)
- [ ] Criar pasta `evidencias/` com screenshot do Accepted
- [ ] Criar pasta `apresentacao/` com `apresentacao.pdf`
- [x] Pasta `src/` com todos os arquivos necessários
- [x] Pasta `dados/` com entrada do problema
- [ ] Adicionar `.gitignore` (excluir `__pycache__/`)
- [ ] Repositório público no GitHub

### README.md (0,25 pts)
- [x] Nome do problema
- [x] Link do problema
- [x] Integrantes do grupo
- [x] Linguagem utilizada
- [x] Como executar a solução
- [x] Explicação da modelagem (vértices, arestas, pesos)
- [x] Algoritmo utilizado (Dijkstra modificado)
- [x] Variação de Dijkstra usada (k extrações por vértice)
- [x] Análise de complexidade (tempo e espaço)
- [ ] Imagem/link comprovando o Accepted ⚠️ *depende da submissão*

---

## 🟡 Apresentação (vale 1,0 pt)

### Slides — `apresentacao/apresentacao.pdf` (0,80 pts)
- [ ] Slide 1: Título + problema + integrantes (~1 min)
- [ ] Slide 2: Modelagem como grafo (vértices=cidades, arestas=voos, pesos=preços) (~1 min)
- [ ] Slide 3: Estratégia Dijkstra modificado (k extrações, heapq, count[v]) (~2 min)
- [ ] Slide 4: Complexidade O(k·m·log(k·m)) tempo, O(n+k·m) espaço (~0.5 min)
- [ ] Slide 5: Casos especiais (ciclos, custos iguais) + Accepted (~0.5 min)

### Avaliação dos ouvintes (0,20 pts)
- [ ] Ensaiar apresentação (máx 5 min)
- [ ] Cada integrante dominar sua parte
- [ ] Foco em modelagem e lógica, NÃO em código

---

## 📊 Progresso da Nota

| Critério                          | Peso | Status |
|:----------------------------------|:----:|:------:|
| Accepted comprovado               | 0,50 | ❌     |
| Código/evidências/PDF organizados | 0,25 | ❌     |
| README completo                   | 0,25 | 🟡 ~80% (faltam nomes + imagem Accepted) |
| Modelagem na apresentação         | 0,35 | ❌     |
| Estratégia algorítmica            | 0,30 | ❌     |
| Complexidade e casos especiais    | 0,15 | ❌     |
| Avaliação dos ouvintes            | 0,20 | ⏳     |
| **TOTAL ESTIMADO**                |**2,0**| **~0,20/2,0** |

---

## 📝 Log de Atualizações

| Data       | O que foi feito |
|:-----------|:----------------|
| 2026-06-02 | Análise inicial — código pronto, faltam entregas formais |
| 2026-06-02 | ✅ README.md criado (faltam nomes dos integrantes + imagem Accepted) |
| 2026-06-02 | ✅ Nomes preenchidos no README (João Isaías, Luiz Carlos, Ricardo André) |
| 2026-06-02 | ✅ Criado `src/submit_cses.py` — arquivo único para submissão no CSES |
|            | *(próximas atualizações serão registradas aqui)* |
