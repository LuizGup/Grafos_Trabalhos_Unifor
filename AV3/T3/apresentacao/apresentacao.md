# Roteiro de Apresentação - T3 (5 minutos)

## Pessoa 1 (0:00-1:30) - Contexto, modelagem de rede e mapeamento
* **Apresentador:** João Isaías
* **O que mostrar na tela:** O navegador na página do problema [UVa 11045](https://onlinejudge.org/external/110/11045.pdf) (ou [UVA_11045_My_T_shirt_suits_me.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/UVA_11045_My_T_shirt_suits_me.md)) e a tabela de modelagem em [README.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/README.md#L23-L41).
* **Ação:** Apontar para o enunciado das camisetas e voluntários no navegador, e depois alternar para o VS Code exibindo a tabela de vértices e arestas no README.md.
* **Falas:**
  "Neste Trabalho Prático 3, o objetivo é resolver o problema UVa 11045, onde precisamos determinar se é possível distribuir N camisetas de 6 tamanhos diferentes (XXL, XL, L, M, S e XS) para M voluntários de modo que cada um receba exatamente um tamanho que aceite. O estoque de camisetas é igualmente dividido, tendo exatamente N/6 camisetas por tamanho. Modelamos isso como um emparelhamento bipartido com múltiplas cópias e reduzimos para fluxo máximo em redes."
  
  "Na modelagem da rede, criamos 8 + M vértices: a origem S é o vértice 0, os tamanhos são indexados de 1 a 6, os voluntários vão de 7 até 7+M-1, e o sorvedouro T é o vértice 7+M. Conectamos S a cada tamanho com capacidade N/6 (limite do estoque). Cada tamanho é conectado aos voluntários que o aceitam com capacidade 1. E cada voluntário é conectado a T com capacidade 1, garantindo que ninguém receba mais de uma camiseta. Se conseguirmos escoar fluxo suficiente de S até T, significa que existe uma atribuição válida para todos."

## Pessoa 2 (1:30-3:20) - Algoritmo, grafo residual e implementação
* **Apresentador:** Luiz Carlos
* **O que mostrar na tela:** O arquivo [ford_fulkerson.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/ford_fulkerson.py#L10-L54) (destacando a busca de caminhos aumentantes via DFS e o grafo residual) e [flow_edge.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/flow_edge.py#L34-L48).
* **Ação:** Mostrar no VS Code os métodos `residual_capacity_to` e `add_residual_flow_to` em `flow_edge.py` e a busca por caminhos aumentantes usando DFS em `ford_fulkerson.py`.
* **Falas:**
  "Para encontrar o fluxo máximo na nossa rede, implementamos o algoritmo de Ford-Fulkerson usando busca em profundidade (DFS) para encontrar caminhos aumentantes. O ponto central da nossa implementação é o controle do grafo residual por meio das capacidades das arestas e suas respectivas arestas reversas. Na classe FlowEdge, os métodos `residual_capacity_to` e `add_residual_flow_to` atualizam a capacidade e o fluxo tanto no sentido direto quanto no reverso."
  
  "Esse conceito de arestas reversas no grafo residual é fundamental: ele permite que o algoritmo 'desfaça' decisões de alocação anteriores que poderiam bloquear outros voluntários. A DFS percorre a rede residual em busca de caminhos aumentantes a partir de S. Quando não existem mais caminhos residuais conectando a origem ao sorvedouro, o loop principal do Ford-Fulkerson termina, garantindo que alcançamos o valor do fluxo máximo."

## Pessoa 3 (3:20-4:40) - Demonstração prática, execução e validação
* **Apresentador:** Luiz Carlos (demonstração) e Ricardo André
* **O que mostrar na tela:** O arquivo de dados [entradas_do_problema.txt](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/dados/entradas_do_problema.txt), os arquivos de ponto de entrada [main.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/main.py) (ou [submit_uva.py](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/src/submit_uva.py)) e o terminal do VS Code rodando o código.
* **Ação:** Exibir os arquivos de código e o arquivo de entrada. Abrir o terminal e executar o comando de teste local, mostrando a saída `YES`, `NO`, `YES`.
* **Falas:**
  "[Luiz Carlos]: Vou realizar a demonstração da execução prática. Implementamos o script principal em `main.py` e consolidamos no arquivo `submit_uva.py` para submissão no portal. Para tornar a leitura de dados resiliente contra espaços extras ou quebras de linha que costumam causar erros na plataforma do UVa, lemos a entrada inteira via tokens usando `sys.stdin.read().split()`. Agora vou rodar a solução no terminal com a nossa instância exemplo."
  
  "*[Luiz executa o comando:* `Get-Content dados/entradas_do_problema.txt | python src/main.py` *]*"
  
  "[Ricardo André]: Como podemos ver no terminal, o programa retorna YES, NO e YES, exatamente os resultados esperados do exemplo. A conversão do fluxo na resposta final é simples: como cada unidade de fluxo escoado de S a T equivale a um voluntário atendido com sucesso, se o valor final do fluxo máximo for igual a M (o número de voluntários), sabemos que todos foram atendidos e exibimos YES, caso contrário exibimos NO."

## Fechamento (4:40-5:00) - Complexidade, casos especiais e Accepted
* **Apresentador:** Ricardo André
* **O que mostrar na tela:** A seção de complexidade em [README.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/README.md#L79-L88), o roteiro manual [roteiro.md](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/acompanhamento/roteiro.md) e a imagem de aprovação [accepted.png](file:///c:/Users/lcarl/Documents/MyProjects/Grafos_Trabalhos_Unifor/AV3/T3/evidencias/accepted.png) no VS Code.
* **Ação:** Mostrar a seção do README correspondente à complexidade, abrir rapidamente o arquivo roteiro.md mostrando a execução manual passo a passo e exibir o print do Accepted na tela.
* **Falas:**
  "Concluindo, o algoritmo de Ford-Fulkerson com DFS possui complexidade de tempo O(E * f*). Como o fluxo máximo f* é no máximo 30 e a rede tem no máximo 96 arestas, executamos cerca de 2.880 operações por teste, o que é instantâneo e mais leve do que Edmonds-Karp. Também montamos o arquivo `roteiro.md` com o passo a passo manual de uma instância de teste para validação teórica. Por fim, mostramos na tela a comprovação da nossa solução que recebeu status de Accepted no portal oficial do UVa Online Judge. Assim finalizamos a nossa apresentação. Obrigado!"
