public class Main {
    public static void main(String[] args) {
        if (args.length != 2) {
            throw new IllegalArgumentException(
                    "informe dois arquivos de entrada. Ex.: java Main ../dados/arvore1.txt ../dados/arvore2.txt"
            );
        }

        Graph tree1 = new Graph(new In(args[0]));
        Graph tree2 = new Graph(new In(args[1]));

        // 1. Exibir lista de adjacencia da Arvore 1
        StdOut.println("=== Arvore 1 ===");
        StdOut.println(tree1);

        // 2. Exibir lista de adjacencia da Arvore 2
        StdOut.println("=== Arvore 2 ===");
        StdOut.println(tree2);

        // 3. Analisar cada arvore
        TreeIsomorphism analysis1 = new TreeIsomorphism(tree1);
        TreeIsomorphism analysis2 = new TreeIsomorphism(tree2);

        // 4. Validacao
        StdOut.println("=== Validacao ===");
        StdOut.println("Arvore 1: " + analysis1.getValidationMessage());
        StdOut.println("Arvore 2: " + analysis2.getValidationMessage());
        StdOut.println();

        // Se alguma entrada nao eh arvore, interromper
        if (!analysis1.isTree() || !analysis2.isTree()) {
            StdOut.println("=== Veredito ===");
            StdOut.println("Comparacao interrompida: uma ou ambas as entradas nao representam arvores validas.");
            return;
        }

        // 5. Centros
        StdOut.println("=== Centros ===");
        StdOut.println("Arvore 1: " + formatCenters(analysis1.getCenters()));
        StdOut.println("Arvore 2: " + formatCenters(analysis2.getCenters()));
        StdOut.println();

        // 6. Codificacao canonica
        StdOut.println("=== Codificacao canonica ===");
        StdOut.println("Arvore 1: " + analysis1.getCanonicalEncoding());
        StdOut.println("Arvore 2: " + analysis2.getCanonicalEncoding());
        StdOut.println();

        // 7. Veredito final
        boolean isomorphic = analysis1.getCanonicalEncoding().equals(analysis2.getCanonicalEncoding());
        StdOut.println("=== Veredito ===");
        if (isomorphic) {
            StdOut.println("As arvores SAO isomorfas.");
        } else {
            StdOut.println("As arvores NAO sao isomorfas.");
        }
    }

    private static String formatCenters(int[] centers) {
        if (centers.length == 1) {
            return "[" + centers[0] + "] (centro unico)";
        } else {
            return "[" + centers[0] + ", " + centers[1] + "] (dois centros)";
        }
    }
}
