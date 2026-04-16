# Roteiro de Apresentacao - T4 (5 minutos)

## Pessoa 1 (0:00-1:20) - Contexto e problema
"Neste Trabalho Pratico 4, o objetivo e resolver o Problema do Caixeiro Viajante usando duas heuristicas classicas de insercao: nearest insertion e smallest insertion. O foco nao e achar a solucao otima, mas construir bons tours de forma incremental e comparar o comprimento final obtido por cada estrategia. Para isso, o projeto trabalha com pontos 2D, distancia euclidiana sob demanda e uma estrutura simples de tour circular."

"No nosso caso, a entrada segue o formato largura, altura e depois as coordenadas de cada cidade. A instancia sugerida para depuracao e tsp10.txt, porque o trabalho ja traz arquivos de referencia para comparar os resultados das duas heuristicas. Depois disso, a execucao final deve ser feita com usa13509.txt."

## Pessoa 2 (1:20-3:10) - Implementacao e heuristicas
"A implementacao ficou concentrada na classe Tour, como pede a documentacao. Nela, completamos os metodos insertNearest(Point p) e insertSmallest(Point p). Em nearest insertion, a cada nova cidade, primeiro escolhemos a cidade mais proxima do tour atual e depois calculamos a melhor posicao de insercao, aquela que gera o menor aumento no comprimento total."

"Em smallest insertion, a ideia muda: nao escolhemos primeiro a cidade mais proxima. Em vez disso, avaliamos diretamente todas as posicoes possiveis no tour e inserimos a cidade no ponto em que o aumento de custo e menor. Assim, as duas heuristicas usam a mesma estrutura de tour, mas com criterios diferentes de escolha."

"O restante da aplicacao ja vem pronto: Main le o arquivo de entrada, carrega os pontos, construiu os dois tours, imprime a quantidade de pontos e os comprimentos, e por fim chama o visualizador. Tambem usamos a classe Point para representar as cidades e calcular a distancia euclidiana."

## Pessoa 3 (3:10-4:30) - Execucao, validacao e visualizacao
"Na validacao com tsp10.txt, o programa imprime a quantidade de pontos e os comprimentos dos dois tours, e os resultados batem com os arquivos de referencia fornecidos no trabalho. Isso confirma que as insercoes estao sendo feitas corretamente e que o calculo do comprimento do tour esta consistente."

"A visualizacao mostra os pontos da instancia e desenha os dois tours com cores diferentes, permitindo comparar rapidamente o comportamento das heuristicas. O nearest insertion e mostrado em uma cor, o smallest insertion em outra, e os comprimentos aparecem na legenda. Isso ajuda a enxergar nao so a saida numerica, mas tambem a forma como cada heuristica constroi o circuito."

## Fechamento (4:30-5:00)
"Concluindo, o trabalho atende ao que foi proposto: modela as cidades como pontos 2D, calcula distancias sob demanda, implementa nearest insertion e smallest insertion na classe Tour, e exibe os dois tours para comparacao. Na apresentacao final, usamos tsp10.txt para demonstrar o funcionamento e usa13509.txt para a execucao principal do projeto."