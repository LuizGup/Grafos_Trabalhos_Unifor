# Checklist para Nota 10 — T3 (UVA 11045 - My T-shirt suits me)

> Documento de acompanhamento para atingir a nota máxima no Trabalho Prático 3.
> **Grupo J:** (Preencher nomes dos integrantes)
> **Última atualização:** 2026-06-10

---

## 🟢 Código-Fonte e Funcionamento Local (Pronto)

- [x] `src/flow_edge.py` — Classe `FlowEdge` (aresta de fluxo baseada no `algs4`)
- [x] `src/flow_network.py` — Classe `FlowNetwork` (rede com listas de adjacência baseada no `algs4`)
- [x] `src/breadth_first_paths.py` — Classe `BreadthFirstPaths` (BFS para caminho aumentante baseada no `algs4`)
- [x] `src/ford_fulkerson.py` — Classe `FordFulkerson` (algoritmo Edmonds-Karp)
- [x] `src/tshirt_network.py` — Modelagem/construção da rede de camisetas
- [x] `src/main.py` — Ponto de entrada: lê entrada padrão (stdin) e imprime `YES` ou `NO`
- [x] Teste de execução local bem-sucedido com `input.txt` (saída: `YES`, `NO`, `YES`) ✅

---

## 🔴 Submissão e Repositório (vale 1,0 pt)

### Accepted no UVA Online Judge (0,50 pts)
- [ ] Criar conta/logar na plataforma UVA Online Judge (https://onlinejudge.org/)
- [ ] Submeter solução para o problema 11045:
  - *Dica:* Criar uma versão consolidada do código em um único arquivo (ex: `src/submit_uva.py`) para facilitar o upload
- [ ] Obter status **Accepted** ✅
- [ ] Capturar print/screenshot da tela de aprovação e salvar em `evidencias/accepted.png` ⚠️ *(Pendente)*

### Organização do repositório (0,25 pts)
- [ ] Criar pasta `dados/` e mover o arquivo `input.txt` para `dados/entradas_do_problema.txt`
- [ ] Criar pasta `evidencias/` e adicionar `accepted.png`
- [ ] Criar pasta `acompanhamento/` e adicionar `roteiro.md` (ficha de modelagem e execução manual)
- [ ] Criar pasta `apresentacao/` e adicionar `apresentacao.md` ou PDF dos slides
- [ ] Adicionar `.gitignore` para ignorar diretórios como `__pycache__/`
- [ ] Garantir que o repositório no GitHub seja público e acessível

### README.md (0,25 pts)
- [x] Nome e link do problema
- [ ] Nomes dos integrantes do grupo no cabeçalho
- [x] Especificação da linguagem utilizada (Python 3)
- [x] Instruções de como executar localmente
- [x] Explicação detalhada da modelagem (definição de origem, sorvedouro, camadas de vértices, arestas e capacidades)
- [x] Algoritmo utilizado e justificativa (Edmonds-Karp)
- [x] Explicação do papel do grafo residual e arestas reversas
- [x] Como o valor do fluxo máximo é convertido no resultado (`YES` se fluxo máximo == M, senão `NO`)
- [x] Análise de complexidade de tempo e espaço
- [ ] Adicionar imagem comprovando o **Accepted** na seção dedicada no final do README

---

## 🟡 Atividade de Acompanhamento (vale 0,2 pts)

- [ ] Criar a ficha curta em `acompanhamento/roteiro.md` contendo:
  1. Resumo do problema com as próprias palavras
  2. Interpretação precisa de entradas e saídas
  3. Detalhamento da modelagem da rede
  4. Justificativa teórica de Edmonds-Karp frente a Ford-Fulkerson com DFS
  5. Uma instância pequena (ex: Caso 2 do exemplo: $N=6$, $M=4$)
  6. Roteiro de execução passo a passo (BFS, caminhos aumentantes, gargalos, capacidades residuais, arestas reversas)
  7. Verificação e interpretação do resultado
- [ ] Validar a ficha com o professor em sala de aula

---

## 🔵 Apresentação da Solução (vale 0,8 pts)

### Slides — `apresentacao/apresentacao.md` (ou PDF)
- [ ] Slide 1: Título do trabalho, identificação do problema (Grupo J) e integrantes
- [ ] Slide 2: Contexto e modelagem como rede de fluxo (origem $s$, sorvedouro $t$, camadas de tamanhos e voluntários, capacidades)
- [ ] Slide 3: Estratégia algorítmica: Edmonds-Karp, grafo residual, busca por caminhos aumentantes via BFS
- [ ] Slide 4: Interpretação e recuperação da resposta final
- [ ] Slide 5: Complexidade, casos especiais tratados e comprovação do Accepted

### Prática e Avaliação (0,15 pts + 0,65 pts)
- [ ] Ensaiar a apresentação respeitando o limite de **5 minutos**
- [ ] Cada integrante dominar a lógica da modelagem (o foco deve ser na modelagem de fluxo e no algoritmo, NÃO na leitura de código linha por linha)

---

## 📊 Progresso Estimado da Nota

| Critério | Peso | Status | Observação |
| :--- | :---: | :---: | :--- |
| **Accepted Comprovado** | 0,50 | 🔴 *Pendente* | Submeter na plataforma e salvar print |
| **Organização do Repositório** | 0,25 | 🔴 *Pendente* | Reorganizar pastas e arquivos de teste |
| **README.md Completo** | 0,25 | 🟡 *Em Progresso* | Inserir nomes dos integrantes e imagem do accepted |
| **Atividade de Acompanhamento** | 0,20 | 🔴 *Pendente* | Criar ficha `roteiro.md` e validar com professor |
| **Apresentação da Solução** | 0,80 | 🔴 *Pendente* | Criar slides e ensaiar apresentação |
| **TOTAL ESTIMADO** | **2,0** | **~0,25 / 2,0** | **Foco atual: Submissão e Ficha de Acompanhamento** |

---

## 📝 Histórico de Modificações

| Data | Responsável | Ação Realizada |
| :--- | :--- | :--- |
| 2026-06-10 | Antigravity AI | Criação do checklist de acompanhamento e testes locais do código original |
