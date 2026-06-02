# Roteiro de Apresentação (Pitch de 5 Minutos) — CSES Flight Routes

Este roteiro organiza as falas e transições de slides para uma apresentação de no máximo **5 minutos (300 segundos)**. O estilo adotado é o de um **pitch**: direto, dinâmico e focado na modelagem do problema e na lógica do algoritmo, sem leitura cansativa de códigos.

---

## 👥 Divisão de Papéis e Tempo

| Apresentador | Slides | Tópicos | Tempo Estimado |
| :--- | :---: | :--- | :---: |
| **João Isaías** | 1 a 17 | Capa, Contexto do Problema, Entrada e Saída | **~2m 00s (120s)** |
| **Luiz Carlos** | 18 a 26 | O Algoritmo de Dijkstra e Passo a Passo da Resolução | **~2m 00s (120s)** |
| **João Isaías** | 27 a 30 | Análise de Complexidade e Resultados (Status Accepted) | **~1m 00s (60s)** |

*Nota: Ricardo André contribuiu na elaboração e design dos slides, mas não apresentará por motivos de saúde.*

---

## 🎙️ Script Slide a Slide

### PARTE 1 — O Problema (Apresentador: João Isaías)
*Meta: Passar pelos slides de contexto (3-17) de forma contínua e rápida à medida que os elementos surgem na tela.*

#### 🛝 Slide 1 e 2 — Abertura e Grupo (0s a 20s)
* **Tela:** Capa "CSES FLIGHT ROUES" + Integrantes.
* **Foco da Fala:**
  > "Boa noite a todos. Nosso grupo ficou responsável pelo problema **CSES 1196 — Flight Routes** (ou Rotas de Voo). O grupo é composto por mim, João Isaías, pelo Luiz Carlos, e pelo Ricardo André, que nos auxiliou na construção da solução e design dos slides."

#### 🛝 Slides 3 a 8 — Contexto e Modelagem (20s a 65s)
*Nota: Clique nos slides de 3 a 8 sequencialmente em ritmo constante para acompanhar a fala.*
* **Tela:** Surgimento dos elementos (Cidades, Rotas, Custos, Parâmetro K).
* **Foco da Fala:**
  > "O problema nos propõe modelar uma rede de viagens aéreas. Nós o representamos como um **Grafo Direcionado e Ponderado**.
  > * As **Cidades** são os nossos vértices ($V$), numerados de $1$ a $N$.
  > * Os **Voos** unidirecionais são as nossas arestas direcionadas ($A$).
  > * O **Preço** de cada voo representa o peso de cada aresta.
  > Nosso objetivo principal é encontrar as **$K$ rotas de menor custo acumulado** saindo da cidade origem $1$ (Syrjälä) até a cidade destino $N$ (Metsälä), sabendo que o problema permite revisitar cidades e passar pelas mesmas conexões."

#### 🛝 Slides 9 a 14 — O Input do Problema (65s a 95s)
*Nota: Vá clicando à medida que descreve a entrada.*
* **Tela:** Construção da entrada padrão do CSES.
* **Foco da Fala:**
  > "Para alimentar o nosso modelo, a entrada do problema nos dá:
  > * Na primeira linha: o número de cidades $N$, a quantidade de voos $M$ e o parâmetro $K$.
  > * Nas $M$ linhas seguintes: a cidade de origem $A$, a cidade de destino $B$ e o custo $C$ do voop.
  > Como detalhe importante, todos os custos de voo são estritamente positivos, variando de $1$ a $10^9$."

#### 🛝 Slides 15 a 17 — O Output Esperado (95s a 120s)
* **Tela:** Definição do Output.
* **Foco da Fala:**
  > "Como saída, devemos retornar exatamente os **$K$ menores preços de rotas possíveis**, ordenados do mais barato ao mais caro. No caso de exemplo clássico para $K=3$, a saída esperada é `4 4 7`.
  > Agora, o Luiz Carlos vai explicar como implementamos o algoritmo para calcular isso de forma eficiente."

---

### PARTE 2 — A Resolução Algorítmica (Apresentador: Luiz Carlos)
*Meta: Explicar a lógica da variação do Dijkstra sem detalhar código puro, mostrando como a poda funciona de forma intuitiva.*

#### 🛝 Slide 18 e 19 — O Motor: Dijkstra Modificado (120s a 150s)
* **Tela:** Definição do Dijkstra e a Variação para K caminhos.
* **Foco da Fala:**
  > "Como todos os pesos das arestas são positivos, o algoritmo de **Dijkstra** é a escolha ideal. No entanto, o Dijkstra clássico é ganancioso e para assim que encontra o menor caminho único para cada vértice.
  > Para obter os **$K$ caminhos**, nós estendemos essa lógica: permitimos que cada vértice seja extraído da nossa Fila de Prioridade Mínima até $K$ vezes. A $j$-ésima vez que retiramos o destino $N$ do heap representa matematicamente a $j$-ésima rota mais barata até ele."

#### 🛝 Slides 20 a 22 — Inicialização e Origem (150s a 175s)
* **Tela:** Inicialização (`count[v]` zerado) e Ponto de Partida inserindo `(0, 1)` no heap.
* **Foco da Fala:**
  > "Na prática, criamos um vetor auxiliar chamado `count[v]`, que monitora quantas vezes cada cidade $v$ foi processada. 
  > Iniciamos colocando o nosso ponto de partida na Fila de Prioridades com custo zero: inserimos o par `(0, 1)`, representando que estamos na cidade 1 com custo acumulado 0."

#### 🛝 Slides 23 e 24 — Extração, Poda e Relaxamento (175s a 210s)
* **Tela:** Lógica de Extração, Poda se `count[u] > k` e Relaxamento Condicional se `count[v] < k`.
* **Foco da Fala:**
  > "O loop principal retira a rota de menor custo `(dist, u)` do heap. 
  > Aqui entra a nossa **poda crítica**: se a cidade $u$ já foi extraída mais de $K$ vezes, nós descartamos esse caminho imediatamente. Por quê? Porque já conhecemos os $K$ melhores caminhos passando por $u$, logo, qualquer rota subsequente será estritamente pior.
  > Caso contrário, incrementamos o contador de visitas de $u$. Se alcançamos o destino $N$, guardamos esse custo. Se for outro vértice, relaxamos suas arestas vizinhas: calculamos `dist + peso` e jogamos de volta no heap apenas se o vizinho $v$ tiver sido visitado menos de $K$ vezes."

#### 🛝 Slides 25 e 26 — Lista Final (210s a 240s)
* **Tela:** Obtenção da lista final dos K menores custos.
* **Foco da Fala:**
  > "Repetimos esse processo até encontrarmos os $K$ caminhos para o destino $N$ ou a fila esvaziar. Como a Fila de Prioridade sempre nos dá o menor custo acumulado primeiro, garantimos que os primeiros $K$ caminhos que chegam a $N$ são os $K$ ótimos ordenados. 
  > Vou devolver a palavra para o João Isaías explicar a complexidade desse processo."

---

### PARTE 3 — Complexidade e Conclusão (Apresentador: João Isaías)

#### 🛝 Slide 27 e 28 — Análise de Complexidade (240s a 270s)
* **Tela:** $\mathcal{O}(K \cdot M \log(K \cdot M))$.
* **Foco da Fala:**
  > "Analisando a eficiência da nossa solução:
  > * **Tempo:** No pior caso, processamos cada uma das $M$ arestas até $K$ vezes. Como as operações de inserção e remoção no heap de tamanho $K \cdot M$ tomam tempo logarítmico, a complexidade temporal fica limitada em $\mathcal{O}(K \cdot M \log(K \cdot M))$. Com $K=10$ e $M=2 \cdot 10^5$, isso roda tranquilamente em menos de **0.6 segundos** no PyPy3.
  > * **Espaço:** Precisamos de $\mathcal{O}(N + M + K \cdot M)$ de memória para representar a lista de adjacência e a fila de prioridades, o que consome uma fração mínima dos 512 MB disponíveis."

#### 🛝 Slide 29 e 30 — Resultados e Encerramento (270s a 300s)
* **Tela:** Evidência do **Accepted** obtido no CSES.
* **Foco da Fala:**
  > "Para validar a solução, nós submetemos o código em Python na plataforma oficial do CSES. O código passou com sucesso em todos os 17 casos de teste da plataforma com status **Accepted**.
  > Com isso, concluímos que o algoritmo modificado resolve o problema de forma robusta e otimizada. Obrigado pela atenção e estamos abertos a perguntas!"

---

## 💡 Dicas de Ouro para o Pitch

1. **Ritmo de Transição:** Os slides de 3 a 17 são extremamente visuais e incrementais. Não pare a fala para passar o slide. Fale continuamente e use o passador de slides como um metrônomo para acompanhar a sua voz.
2. **Postura de Pitch:** Não leia os tópicos do slide. Use os tópicos da tela apenas como âncoras visuais para o público e fale com as suas próprias palavras seguindo a ideia sugerida no roteiro.
3. **Domínio da Lógica:** Foquem em explicar *porque a poda funciona* (não precisamos de mais do que $K$ caminhos em nenhum vértice intermediário) e *porque a fila de prioridades garante a ordenação*. O professor valoriza muito essa intuição matemática sobre o código.
