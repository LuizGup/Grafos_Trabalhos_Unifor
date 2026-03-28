# Roteiro de Apresentacao - T2 (2 minutos)

## Pessoa 1 (0:00-0:40) - Contexto e objetivo
"Nosso Trabalho Pratico 2 modela o grafo do cavalo em um tabuleiro 3x3. Cada casa do tabuleiro e um vertice e existe aresta entre duas casas quando o cavalo chega em um unico movimento. A numeracao dos vertices segue a ordem de leitura da matriz, de 0 a 8. O objetivo e aplicar conceitos de grafos para responder lista de adjacencia, componentes conexas, distancia minima, existencia de ciclo e um ciclo encontrado." 

## Pessoa 2 (0:40-1:20) - Implementacao
"A entrada foi montada no formato algs4 com V, E e as arestas em dados/entrada.txt. No codigo, usamos graph.py para lista de adjacencia, cc.py para componentes conexas e cycle.py para detectar ciclo e retornar os vertices de um ciclo. No main.py, lemos o arquivo, imprimimos o grafo, calculamos as componentes e usamos BFS para obter a distancia minima entre os vertices 0 e 8, que representam as posicoes (0,0) e (2,2)." 

## Pessoa 3 (1:20-2:00) - Resultados e conclusao
"Nosso resultado final mostra a lista de adjacencia esperada, 2 componentes conexas, com a componente isolada no vertice 4, distancia minima de 4 movimentos entre 0 e 8, e confirma que o grafo possui ciclo. Tambem exibimos um ciclo valido: 0 5 6 1 8 3 2 7 0. Para a analise pedida, informamos a complexidade do algoritmo de ciclo por DFS: tempo O(V + E) e espaco O(V). Concluimos que a solucao atende todos os requisitos do enunciado do T2." 

## Fechamento (frase final)
"Implementamos todos os pontos exigidos no T2 com saida clara e validada."