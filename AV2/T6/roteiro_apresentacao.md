# Roteiro de Apresentacao - T6 (5 minutos)

## Pessoa 1 (0:00-1:30) - Isomorfismo, motivacao e codificacao canonica

"Neste Trabalho Pratico 6, o objetivo e determinar se duas arvores nao direcionadas sao isomorfas. Duas arvores sao isomorfas quando possuem exatamente a mesma estrutura de adjacencia, mesmo que os rotulos dos vertices sejam diferentes. Ou seja, existe uma correspondencia entre os vertices que preserva todas as conexoes."

"Comparar apenas o numero de vertices, arestas ou a sequencia de graus nao e suficiente para decidir isomorfismo. Duas arvores podem ter a mesma sequencia de graus e ainda assim ter organizacoes internas diferentes. Por isso, usamos a tecnica de codificacao canonica: transformamos cada arvore em uma representacao textual unica, independente da rotulacao dos vertices. Se as duas codificacoes forem iguais, as arvores sao isomorfas; caso contrario, nao sao."

## Pessoa 2 (1:30-3:20) - Centro, enraizamento e algoritmo de codificacao

"Para que a codificacao seja canonica, precisamos enraizar a arvore em um ponto especial: o centro. O centro e encontrado por remocao iterativa de folhas: a cada passo, removemos todas as folhas da arvore e atualizamos os graus dos vizinhos. Os ultimos vertices restantes sao os centros. Uma arvore pode ter um ou dois centros."

"Depois de encontrar o centro, enraizamos a arvore nele e aplicamos a codificacao recursiva. Para cada vertice, codificamos recursivamente todos os seus filhos. As codificacoes dos filhos sao ordenadas lexicograficamente e concatenadas entre parenteses. Uma folha recebe o codigo '()'. Essa ordenacao e fundamental: sem ela, a mesma arvore poderia gerar codificacoes diferentes dependendo da ordem em que os filhos aparecem na lista de adjacencia. A ordenacao garante que a codificacao e unica para a estrutura."

"Quando a arvore tem dois centros, enraizamos em cada um deles, geramos as duas codificacoes e escolhemos a menor lexicograficamente. Isso garante consistencia independente de qual centro for escolhido."

## Pessoa 3 (3:20-4:40) - Implementacao, validacao e execucao

"Na implementacao, concentramos tudo na classe TreeIsomorphism. Primeiro, validamos se a entrada e uma arvore: verificamos que o numero de arestas e igual a V menos 1 e que o grafo e conexo usando BFS. Se a entrada nao for valida, como um ciclo, o programa interrompe e informa o motivo."

"Na execucao, testamos quatro cenarios. No primeiro, dois caminhos de 4 vertices com rotulacoes diferentes: ambos tem dois centros e a mesma codificacao canonica, entao sao isomorfas. No segundo, um caminho de 5 contra uma estrela de 5: ambos sao arvores validas, mas as codificacoes sao diferentes, entao nao sao isomorfas. No terceiro, duas arvores de 7 vertices com centro unico: mesma codificacao, isomorfas. No quarto, um ciclo de 3 vertices: o programa detecta que nao e arvore e interrompe a comparacao."

## Fechamento (4:40-5:00)

"Concluindo, a tecnica de codificacao canonica garante uma decisao correta de isomorfismo porque transforma cada arvore em uma representacao unica baseada na sua estrutura real, nao nos rotulos. A ordenacao lexicografica dos codigos dos filhos e essencial para eliminar qualquer dependencia da ordem de leitura das arestas. O trabalho atende ao que foi proposto: validacao das entradas, calculo dos centros, codificacao canonica e veredito final."
