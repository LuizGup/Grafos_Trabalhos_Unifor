# UVa 11045 — My T-shirt suits me
### Apresentação e Roteiro de Falas — Grupo J

---

## 1. Contexto e objetivo (1 min)

**Conteúdo do Slide:**
* **Problema:** Distribuir $N$ camisetas ($N/6$ de cada um dos 6 tamanhos) para $M$ voluntários.
* Cada voluntário aceita exatamente 2 tamanhos. É possível atender a todos?
* **Objetivo:** Verificar se existe uma distribuição válida $\to$ `YES` ou `NO`.
* **Redução:** Emparelhamento bipartido com múltiplas cópias por tamanho, resolvido via fluxo máximo.

---
### 🎙️ Roteiro da Fala (Slide 1)
* **Apresentador:** João Isaías
* **Ação:** Exibir o primeiro slide, se apresentar e abrir na tela o arquivo com o enunciado do problema: [UVA_11045_My_T_shirt_suits_me.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/UVA_11045_My_T_shirt_suits_me.md).
* **Falas:**
  > "Boa noite, pessoal! Nosso grupo ficou responsável pelo problema **UVa 11045 — My T-shirt suits me**.
  > O contexto do problema é o seguinte: temos $N$ camisetas em estoque, divididas igualmente em 6 tamanhos (`XXL`, `XL`, `L`, `M`, `S` e `XS`). Temos também $M$ voluntários que precisam de uma camiseta cada. O desafio é que cada voluntário só aceita receber exatamente dois tamanhos específicos.
  > Nosso objetivo é determinar se é possível fazer uma distribuição que atenda a todos. Para resolver isso, modelamos o problema como um **emparelhamento bipartido com múltiplas cópias**, o qual reduziremos diretamente para um problema de **fluxo máximo em redes**."

---

## 2. Modelagem da rede de fluxo (1 min)

**Conteúdo do Slide:**
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
* **Fonte $\to$ tamanho:** limita o estoque ($N/6$ unidades por tamanho).
* **Tamanho $\to$ voluntário:** capacidade = 1 (se o voluntário aceita o tamanho).
* **Voluntário $\to$ sorvedouro:** capacidade = 1 (garante 1 camiseta por pessoa).

---
### 🎙️ Roteiro da Fala (Slide 2)
* **Apresentador:** João Isaías
* **Ação:** Apontar para o diagrama de fluxo na tela e detalhar as conexões abrindo a seção de modelagem do [README.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/README.md#L23-L41).
* **Falas:**
  > "Para modelar essa rede de fluxo, criamos uma estrutura com $8 + M$ vértices.
  > Primeiro, temos a **Fonte S** (vértice 0), conectada aos 6 nós de tamanhos de camiseta. A capacidade de cada aresta é de $N/6$, o que limita a quantidade máxima que podemos tirar de cada estoque.
  > Depois, conectamos cada tamanho de camiseta aos voluntários que o aceitam, com capacidade $1$.
  > Por fim, conectamos cada voluntário ao **Sorvedouro T** (vértice $7+M$) com capacidade $1$, garantindo que nenhum voluntário receba mais de uma camiseta. Se conseguirmos escoar fluxo suficiente de S até T, significa que conseguimos alocar as camisas de forma que todos sejam atendidos."

---

## 3. Algoritmo e grafo residual (1 min)

**Conteúdo do Slide:**
* **Algoritmo:** Ford-Fulkerson com DFS (busca em profundidade) para encontrar caminhos aumentantes.
* **Grafo residual:** arestas reversas permitem "desfazer" alocações.
  * Se $V_2$ tomou o tamanho $L$, mas $V_3$ precisa de $L$ exclusivamente, o algoritmo redireciona o fluxo pela aresta reversa.
* **Condição de parada:** nenhum caminho $S \to T$ no grafo residual.

---
### 🎙️ Roteiro da Fala (Slide 3)
* **Apresentador:** Luiz Carlos
* **Ação:** Apresentar a lógica do algoritmo e o papel fundamental das arestas reversas exibindo o arquivo [ford_fulkerson.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/ford_fulkerson.py#L32-L51) (especialmente a busca de caminhos residuais).
* **Falas:**
  > "Boa noite! Eu vou explicar a estratégia algorítmica. Escolhemos usar o método de **Ford-Fulkerson** com Busca em Profundidade (**DFS**) para encontrar caminhos aumentantes de $S$ até $T$.
  > O ponto crucial do nosso código é a manutenção do **grafo residual**. A cada caminho aumentante encontrado, nós empurramos fluxo pelo gargalo do caminho e atualizamos as capacidades residuais. As arestas reversas desempenham um papel essencial aqui: elas nos permitem desfazer alocações ruins feitas em passos anteriores. Se um voluntário pegou uma camiseta que outro voluntário precisa obrigatoriamente, o fluxo é desviado através de uma aresta reversa para buscar outra opção viável.
  > O loop termina no momento em que a DFS não consegue mais encontrar nenhum caminho da origem ao sorvedouro no grafo residual."

---

## 4. Demonstração Prática do Código (1 min)

**Conteúdo do Slide:**
* **Classes baseadas no `algs4`:** `FlowEdge`, `FlowNetwork` e `FordFulkerson`.
* **Submissão Consolidada:** `submit_uva.py` unificando toda a estrutura.
* **Execução local:**
  ```bash
  Get-Content dados/entradas_do_problema.txt | python src/main.py
  ```

---
### 🎙️ Roteiro da Fala (Slide 4 - Demonstração)
* **Apresentador:** Luiz Carlos
* **Ação:** Compartilhar a tela exibindo os arquivos de código [flow_edge.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/flow_edge.py), [flow_network.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/flow_network.py), [main.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/main.py) e o consolidado [submit_uva.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/submit_uva.py). Mostrar também o arquivo de dados [entradas_do_problema.txt](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/dados/entradas_do_problema.txt) antes de executar o script no terminal.
* **Falas:**
  > "Vou mostrar rapidamente nossa implementação no VS Code. Nós temos os arquivos `flow_edge.py`, `flow_network.py` e `ford_fulkerson.py`, que seguem a mesma lógica das classes do livro *Algorithms 4th Edition* (Sedgewick & Wayne).
  > Também consolidamos tudo em um único arquivo, o `submit_uva.py`, para facilitar o envio no portal Online Judge.
  > *[Luiz executa o comando no terminal: `Get-Content dados/entradas_do_problema.txt | python src/main.py`]*
  > Como vocês podem ver, para o nosso arquivo de testes, a resposta emitida é `YES`, `NO` e `YES`, correspondendo exatamente à saída esperada pelo problema."

---

## 5. Conversão do fluxo na resposta (30 seg)

**Conteúdo do Slide:**
* Cada unidade de fluxo = 1 voluntário que recebeu uma camiseta adequada.
* Se fluxo máximo == $M \implies$ **YES** (todos atendidos).
* Se fluxo máximo < $M \implies$ **NO** (falta de estoque em tamanhos compatíveis).
* Não é preciso reconstruir o emparelhamento, o valor do fluxo máximo é suficiente.

---
### 🎙️ Roteiro da Fala (Slide 5)
* **Apresentador:** Ricardo André
* **Ação:** Retomar a apresentação dos slides e detalhar a lógica mostrando o trecho em [main.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/main.py#L46-L47) (ou no consolidado [submit_uva.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/submit_uva.py#L138-L139)) que converte o fluxo na resposta final.
* **Falas:**
  > "Boa noite a todos. Eu vou explicar como interpretamos o resultado da nossa rede.
  > Cada unidade de fluxo que escoa com sucesso de S para T representa exatamente um voluntário que recebeu uma camiseta que lhe serve.
  > Portanto, se o valor do fluxo máximo final calculado pelo algoritmo for exatamente igual a $M$ (o número de voluntários), temos a garantia de que todos foram atendidos, e exibimos `YES`. Caso o fluxo máximo seja menor que $M$, exibimos `NO` porque, devido a restrições de estoque de determinados tamanhos, algum voluntário ficou sem camiseta."

---

## 6. Complexidade, Casos Especiais e Conclusão (30 seg)

**Conteúdo do Slide:**
* **Complexidade de tempo:** $O(E \cdot f^*)$ onde $f^* \le M \le 30$.
  * No pior caso: $96 \times 30 = 2.880$ operações (execução instantânea).
* **Por que não Edmonds-Karp (BFS)?** Edmonds-Karp teria custo teórico de $O(V \cdot E^2) \approx 350.000$ operações. Para fluxos pequenos, o Ford-Fulkerson com DFS é mais simples de implementar e extremamente rápido.
* **Evidência de Aprovação:** Status **Accepted** no portal UVA Online Judge.

---
### 🎙️ Roteiro da Fala (Slide 6)
* **Apresentador:** Ricardo André
* **Ação:** Mostrar o slide com a análise de complexidade, exibir o arquivo [roteiro.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/acompanhamento/roteiro.md) no repositório com o passo a passo manual, e apontar para o print do Accepted em [accepted.png](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/evidencias/accepted.png).
* **Falas:**
  > "Para concluir, analisando a complexidade, a nossa rede possui no máximo 38 vértices e 96 arestas. Como o fluxo máximo é pequeno ($f^* \le 30$), o Ford-Fulkerson clássico com busca por DFS tem complexidade $O(E \cdot f^*)$, executando em menos de 3 mil operações — muito mais rápido e simples do que Edmonds-Karp neste caso.
  > Tratamos com sucesso casos de teste múltiplos e entradas com espaços adicionais usando uma leitura otimizada por tokens.
  > Aqui no slide vocês podem ver a comprovação da nossa submissão com status **Accepted** no portal do UVa Online Judge. Obrigado pela atenção!"
