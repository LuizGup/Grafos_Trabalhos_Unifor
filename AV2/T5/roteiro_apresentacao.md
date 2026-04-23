# Roteiro de Apresentacao - T5 (5 minutos)

## Pessoa 1 (0:00-1:30) - Contexto, modelagem e Teorema das 4 Cores

"Neste Trabalho Pratico 5, o objetivo e aplicar o algoritmo DSatur para colorir o mapa politico do Brasil, modelado como um grafo nao direcionado. Cada estado e um vertice e cada fronteira terrestre entre dois estados e uma aresta. O problema de coloracao de mapas consiste em atribuir cores aos vertices de modo que nenhum par de vizinhos tenha a mesma cor, usando o menor numero de cores possivel."

"Na modelagem, usamos 27 vertices, um para cada estado, indexados em ordem alfabetica por sigla: AC e 0, AL e 1, e assim por diante ate TO, que e 26. Construimos o arquivo brasil.txt no formato algs4, com 51 arestas representando as fronteiras terrestres entre estados. O grafo resultante e planar, e pelo Teorema das Quatro Cores, admite coloracao com no maximo quatro cores. Esse teorema garante a existencia da solucao, mas nao e um algoritmo: a nossa tarefa e aplicar o DSatur como heuristica para obter uma coloracao valida e de boa qualidade."

## Pessoa 2 (1:30-3:20) - Algoritmo DSatur e implementacao

"O DSatur e uma heuristica gulosa para coloracao de vertices. A diferenca dele para outras heuristicas e o uso do grau de saturacao: o DS de um vertice v e o numero de cores distintas ja presentes na vizinhanca de v. Isso significa que o DS mede o quanto um vertice esta restrito pela coloracao parcial ja construida."

"A cada passo, o algoritmo escolhe o vertice nao colorido com maior DS. Em caso de empate, usamos o maior grau como criterio de desempate, porque um vertice com mais vizinhos tem maior potencial de conflito. Depois de escolher o vertice, atribuimos a menor cor disponivel que nao conflite com os vizinhos ja coloridos."

"Na implementacao, concentramos tudo na classe GraphColoringDSatur. O metodo color() executa o algoritmo: primeiro colore o vertice de maior grau com a cor 1, depois, em cada iteracao, calcula o DS de todos os vertices nao coloridos, escolhe o de maior DS com desempate por grau e atribui a menor cor viavel. Usamos um HashSet para rastrear as cores dos vizinhos ao calcular o DS e ao encontrar a menor cor disponivel. Alem disso, implementamos os metodos getColor, getColorCount, getColoringOrder, isValidColoring e getLabel para exibicao e validacao."

## Pessoa 3 (3:20-4:40) - Execucao, resultados e validacao

"Na execucao com brasil.txt, o programa carrega o grafo com 27 vertices e 51 arestas, exibe a lista de adjacencia, executa o DSatur e mostra a ordem de coloracao. O primeiro vertice colorido e BA, porque tem o maior grau, com 8 vizinhos. Em seguida vem MG, GO, TO e assim por diante, sempre priorizando os vertices mais saturados."

"O resultado final mostra que o mapa foi colorido com 4 cores, e o programa confirma que a coloracao e valida, ou seja, nenhum par de estados vizinhos recebeu a mesma cor. Nos testes com os fixtures, o comportamento tambem ficou correto: o triangulo usou 3 cores, o caminho de 4 vertices usou 2, o ciclo par usou 2 e o ciclo impar usou 3, todos resultados esperados."

"A validacao e feita percorrendo todas as arestas do grafo: para cada aresta v-w, verificamos se as cores de v e w sao diferentes. Se todas forem, a coloracao e valida."

## Fechamento (4:40-5:00)

"Concluindo, o DSatur e considerado heuristico porque nao garante sempre o numero minimo de cores; ele produz uma coloracao valida e frequentemente de boa qualidade, mas nao existe garantia de otimalidade para todo grafo. No nosso caso, o DSatur encontrou 4 cores para o mapa do Brasil, o que e consistente com o Teorema das Quatro Cores. O trabalho atende ao que foi proposto: modelagem correta das fronteiras terrestres, implementacao do DSatur, exibicao da ordem de coloracao, das cores atribuidas e da validacao final."
