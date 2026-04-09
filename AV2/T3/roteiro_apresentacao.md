# Roteiro de Apresentacao - T3 (2 a 4 minutos)

## Pessoa 1 (0:00-0:50) - Contexto e objetivo
"Nosso Trabalho Pratico 3 trata do Problema do Carteiro Chines em um digrafo ponderado. A ideia e encontrar um circuito euleriano em um grafo ja eulerizado. Para isso, primeiro analisamos manualmente o grafo oficial, identificamos os vertices desbalanceados e montamos o arquivo entrada_eulerizada.txt. Depois, no codigo, aplicamos o metodo de Hierholzer para obter o circuito euleriano e calcular o custo total."

## Pessoa 2 (0:50-1:50) - Parte manual e estrutura da solucao
"Na parte manual, usamos o grafo da figura do enunciado para calcular os graus de entrada e saida de cada vertice. Quando o grau de entrada e o grau de saida nao coincidem, o vertice esta desbalanceado. Como o enunciado nao pede Floyd-Warshall nem emparelhamento otimo implementado, essa etapa foi feita na construcao da entrada eulerizada, repetindo arestas ou caminhos para equilibrar o grafo. No codigo, organizamos a solucao em digraph.py, com a classe do digrafo ponderado, hierholzer.py, com a implementacao do algoritmo, e main.py, que le a entrada, mostra os graus, verifica o balanceamento e executa a busca do circuito."

## Pessoa 3 (1:50-3:10) - Resultados e conclusao
"Na execucao, o programa mostra a lista de adjacencia do grafo, os graus de entrada e saida de cada vertice, confirma que todos estao balanceados e, em seguida, exibe o circuito euleriano encontrado. Tambem informamos o custo total do percurso, que corresponde a soma dos pesos de todas as arestas visitadas. Nos testes com os arquivos de exemplo, o algoritmo encontrou circuitos validos e confirmou o comportamento esperado. Assim, a solucao atende ao que foi pedido: modelagem do digrafo ponderado, eulerizacao manual e aplicacao do metodo de Hierholzer."

## Fechamento
"Concluimos que o grafo final ficou balanceado, admitiu circuito euleriano e a implementacao retorna o percurso fechado e seu custo total."
