# Roteiro de Apresentação ao Vivo (Sem Slides) — Grupo J
**Problema:** UVa 11045 — My T-shirt suits me  
**Integrantes:** João Isaías, Luiz Carlos e Ricardo André  

---

## Estrutura da Apresentação
Como a apresentação será feita diretamente no computador, sem uso de slides, a dinâmica será baseada no compartilhamento da tela do **Navegador** (página do problema) e do **VS Code** (arquivos de código, README, roteiro manual e execução no terminal).

---

### 🟢 Parte 1: Introdução e Contexto do Problema (João Isaías)
* **Tempo estimado:** ~1 minuto
* **O que mostrar na tela:** O navegador aberto na página oficial do problema: [UVa 11045 - PDF](https://onlinejudge.org/external/110/11045.pdf) ou o arquivo markdown [UVA_11045_My_T_shirt_suits_me.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/UVA_11045_My_T_shirt_suits_me.md).
* **Ação do Apresentador:** Explicar a regra do problema apontando para o enunciado.
* **Roteiro da Fala (João Isaías):**
  > "Boa noite, professor e colegas. Nós somos o Grupo J e vamos apresentar a nossa resolução para o problema **UVa 11045 — My T-shirt suits me**.
  > O contexto do problema é o seguinte: o instrutor de um programa de voluntários precisa distribuir N camisetas de 6 tamanhos diferentes (XXL, XL, L, M, S e XS) para M voluntários. O estoque é igualmente dividido entre os 6 tamanhos, ou seja, temos exatamente N/6 camisetas de cada tamanho.
  > Cada voluntário aceita apenas dois tamanhos específicos de camisetas. Nosso objetivo é decidir se é possível fazer uma distribuição válida que atenda a todos os voluntários, imprimindo YES ou NO."

---

### 🟢 Parte 2: Modelagem da Rede de Fluxo (João Isaías)
* **Tempo estimado:** ~1 minuto
* **O que mostrar na tela:** O arquivo [README.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/README.md#L22-L41) na seção de **Modelagem como Rede de Fluxo** (exibindo a tabela de vértices, arestas e capacidades).
* **Ação do Apresentador:** Percorrer a tabela de vértices e arestas explicando o modelo teórico de rede de fluxo.
* **Roteiro da Fala (João Isaías):**
  > "Para resolver esse emparelhamento bipartido com múltiplos recursos, modelamos o problema como uma rede de fluxo direcionada.
  > Como vocês podem ver aqui na tabela do nosso README:
  > - Criamos a **Origem (S)** no vértice 0.
  > - Conectamos S a cada um dos 6 tamanhos de camiseta, com capacidade N/6 (que representa o limite do estoque por tamanho).
  > - Conectamos cada tamanho de camiseta aos voluntários correspondentes que aceitam aquele tamanho, com capacidade 1 (pois um voluntário só consome uma camiseta daquela opção).
  > - E conectamos cada nó de voluntário ao **Sorvedouro (T)** com capacidade 1, garantindo que nenhum voluntário receba mais de uma camiseta.
  > Dessa forma, se conseguirmos escoar fluxo suficiente de S até T, temos uma atribuição válida."

---

### 🟢 Parte 3: Algoritmo e Grafo Residual (Luiz Carlos)
* **Tempo estimado:** ~1 minuto
* **O que mostrar na tela:** O VS Code exibindo os arquivos de implementação [ford_fulkerson.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/ford_fulkerson.py#L10-L54) e o conceito de aresta residual em [flow_edge.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/flow_edge.py#L34-L48).
* **Ação do Apresentador:** Mostrar o código e explicar a lógica teórica do algoritmo e do grafo residual.
* **Roteiro da Fala (Luiz Carlos):**
  > "Boa noite. Vou explicar como implementamos o algoritmo. Escolhemos usar o método clássico de **Ford-Fulkerson** com Busca em Profundidade (DFS) para encontrar caminhos aumentantes.
  > O grande diferencial do fluxo máximo está na utilização do **Grafo Residual**. Aqui no código da classe `FlowEdge`, vocês podem ver os métodos `residual_capacity_to` e `add_residual_flow_to`. Eles controlam o fluxo na aresta direta e o fluxo residual na aresta reversa.
  > Essas arestas reversas funcionam como um mecanismo de 'desfazer'. Se o algoritmo faz uma atribuição ruim no início (por exemplo, alocando um tamanho para um voluntário que aceitaria outra opção), ele consegue redirecionar esse fluxo no grafo residual por meio das arestas reversas, encontrando novos caminhos aumentantes até que nenhum caminho de S a T seja mais alcançável pela DFS."

---

### 🟢 Parte 4: Leitura dos Dados e Execução Local (Luiz Carlos)
* **Tempo estimado:** ~1 minuto
* **O que mostrar na tela:** O arquivo [main.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/main.py) (ou o arquivo consolidado de submissão [submit_uva.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/submit_uva.py)) e o terminal do VS Code.
* **Ação do Apresentador:** Explicar a leitura robusta de entrada e rodar o script localmente no terminal.
* **Roteiro da Fala (Luiz Carlos):**
  > "Aqui no arquivo de ponto de entrada (`main.py`), fazemos a leitura rápida dos casos de teste. Na nossa versão final para submissão (`submit_uva.py`), utilizamos uma leitura por tokens baseada em `sys.stdin.read().split()`. Fizemos isso para garantir o correto tratamento de espaços em branco ou quebras de linha que o juiz do UVa costuma incluir.
  > Vou rodar os testes da pasta de dados localmente no terminal:
  > *[Luiz executa o comando no terminal do VS Code:* `Get-Content dados/entradas_do_problema.txt | python src/main.py` *]*
  > Como podem ver, a saída local do nosso programa para o caso exemplo é `YES`, `NO` e `YES`, batendo exatamente com as respostas oficiais."

---

### 🟢 Parte 5: Interpretação da Resposta e Complexidade (Ricardo André)
* **Tempo estimado:** ~30 segundos
* **O que mostrar na tela:** O trecho final do código no VS Code ([main.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/main.py#L46-L47)) onde o valor do fluxo máximo é comparado com M, e a seção de complexidade no [README.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/README.md#L79-L88).
* **Ação do Apresentador:** Explicar a conversão do fluxo na resposta e falar sobre a complexidade computacional.
* **Roteiro da Fala (Ricardo André):**
  > "Boa noite a todos. Eu vou explicar como interpretamos o resultado. 
  > A quantidade máxima de fluxo que chega ao sorvedouro representa exatamente quantos voluntários conseguiram receber uma camiseta que lhes serve.
  > Como a nossa condição é que *todos* os voluntários sejam atendidos, o fluxo máximo calculado deve ser exatamente igual a M (o número de voluntários). Se `ff.value() == M`, imprimimos YES, caso contrário, NO.
  > Em termos de complexidade de tempo, o Ford-Fulkerson com DFS roda em O(E * f*). Como o fluxo máximo é no máximo M (onde M <= 30) e temos pouquíssimas arestas (E <= 96), no pior caso executamos apenas cerca de 2.880 operações por caso de teste. Por isso, a escolha do Ford-Fulkerson clássico com DFS é perfeita e muito mais leve de implementar do que o algoritmo de Edmonds-Karp (BFS) para esta dimensão de rede."

---

### 🟢 Parte 6: Roteiro Manual e Accepted (Ricardo André)
* **Tempo estimado:** ~30 segundos
* **O que mostrar na tela:** O arquivo markdown do roteiro da atividade de acompanhamento [roteiro.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/acompanhamento/roteiro.md) e o print do Accepted em [accepted.png](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/evidencias/accepted.png) no VS Code.
* **Ação do Apresentador:** Mostrar o passo a passo manual rápido e a imagem com o status Accepted da plataforma.
* **Roteiro da Fala (Ricardo André):**
  > "Para a atividade de acompanhamento, detalhamos neste documento (`roteiro.md`) uma simulação manual de execução passo a passo do algoritmo de caminhos aumentantes no segundo caso de teste (o que resulta em NO), mostrando cada gargalo e as atualizações do residual.
  > E para finalizar, mostro a imagem de comprovação contida na pasta de evidências do repositório, atestando que a nossa submissão foi aceita com o status de **Accepted** no portal do UVa Online Judge.
  > Com isso, concluímos a nossa apresentação. Obrigado a todos!"
