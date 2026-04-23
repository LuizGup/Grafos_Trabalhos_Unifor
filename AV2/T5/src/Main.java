public class Main {
    public static void main(String[] args) {
        if (args.length < 1) {
            throw new IllegalArgumentException(
                    "informe o arquivo de entrada. Ex.: java Main ../dados/brasil.txt"
            );
        }

        In in = new In(args[0]);
        Graph graph = new Graph(in);
        GraphColoringDSatur dsatur = new GraphColoringDSatur(graph);

        // 1. Exibir o grafo (lista de adjacencia)
        StdOut.println("=== Grafo carregado ===");
        StdOut.println(graph);

        // 2. Executar o algoritmo DSatur
        dsatur.color();

        // 3. Exibir a ordem de coloracao
        StdOut.println("=== Ordem de coloracao ===");
        int[] order = dsatur.getColoringOrder();
        for (int i = 0; i < order.length; i++) {
            StdOut.printf("  %2d. %s (vertice %2d)%n",
                    i + 1, dsatur.getLabel(order[i]), order[i]);
        }
        StdOut.println();

        // 4. Exibir as cores finais de cada vertice
        StdOut.println("=== Cores atribuidas ===");
        for (int v = 0; v < graph.V(); v++) {
            StdOut.printf("  %s (vertice %2d): cor %d%n",
                    dsatur.getLabel(v), v, dsatur.getColor(v));
        }
        StdOut.println();

        // 5. Exibir o total de cores utilizadas
        StdOut.printf("Total de cores utilizadas: %d%n", dsatur.getColorCount());

        // 6. Validar se a coloracao produzida eh valida
        boolean valid = dsatur.isValidColoring();
        StdOut.printf("Coloracao valida: %s%n", valid ? "SIM" : "NAO");
    }
}
