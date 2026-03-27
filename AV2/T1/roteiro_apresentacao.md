# Roteiro de Apresentacao - T1 (2 minutos)

## Contexto e objetivo
  Nosso Trabalho Prático 1 é sobre grafos, com os estados do Nordeste como vértices e as fronteiras terrestres como arestas.
  
  O enunciado pede implementar DFS e BFS e responder seis pontos principais: se um estado alcança outro, caminho encontrado por DFS, caminho por BFS, estados alcançáveis a partir da origem, ordem de visita da DFS e ordem de visita da BFS.
  
  Também seguimos os requisitos de usar lista de adjacência, mapear os estados em ordem alfabética e permitir entrada de origem e destino.

## Implementacao da solucao
  A gente modelou o grafo com os 9 estados da região Nordeste e carregou as fronteiras pelo arquivo de dados.

  A entrada é simples: o usuário digita estado de origem e destino, com validação de sigla. Depois executamos os dois algoritmos: a DFS para explorar em profundidade e a BFS para encontrar o caminho com menor número de arestas.

  Além dos caminhos, registramos a ordem de visita de cada busca, que é um ponto importante de comparação pedido pelo enunciado." 

## Resultados e conclusao
  Nosso programa entrega exatamente as 6 respostas exigidas no T1, de forma clara na saída.
  
  A conectividade entre origem e destino é verificada, os dois caminhos são mostrados e os estados alcançáveis também.

  Com isso, conseguimos comparar o comportamento da DFS e da BFS na prática: a DFS segue um ramo até o fim antes de voltar, enquanto a BFS expande por níveis e tende ao caminho mínimo em número de fronteiras 

  Conclusão: a solução atende os requisitos técnicos e cumpre o objetivo do trabalho de aplicar grafos em um problema real do Nordeste. 

## Fechamento
Atendemos todos os requisitos do enunciado com uma implementacao objetiva e validada.