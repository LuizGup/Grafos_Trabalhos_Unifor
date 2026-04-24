import java.util.ArrayList;
import java.util.Collections;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;

public class TreeIsomorphism {
    private final Graph graph;
    private boolean treeValid;
    private String validationMessage;
    private int[] centers;
    private String canonicalEncoding;
    private boolean analyzed;

    public TreeIsomorphism(Graph graph) {
        if (graph == null) {
            throw new IllegalArgumentException("graph nao pode ser nulo");
        }
        this.graph = graph;
        this.analyzed = false;
        analyze();
    }

    public Graph getGraph() {
        return graph;
    }

    /**
     * Executa toda a analise: validacao, centros e codificacao canonica.
     */
    private void analyze() {
        // 1. Validar se eh arvore
        treeValid = validateTree();

        if (treeValid) {
            // 2. Encontrar centro(s)
            centers = findCenters();

            // 3. Gerar codificacao canonica
            canonicalEncoding = buildCanonicalEncoding();
        }

        analyzed = true;
    }

    // ========== VALIDACAO ==========

    /**
     * Verifica se o grafo eh uma arvore:
     * - V >= 1
     * - E == V - 1
     * - Grafo conexo (BFS a partir do vertice 0 alcanca todos)
     */
    private boolean validateTree() {
        int V = graph.V();
        int E = graph.E();

        if (V == 0) {
            validationMessage = "Entrada invalida: grafo sem vertices";
            return false;
        }

        if (E != V - 1) {
            validationMessage = "Entrada invalida: uma arvore com " + V
                    + " vertices deve ter " + (V - 1) + " arestas, mas tem " + E;
            return false;
        }

        // Verificar conectividade com BFS
        boolean[] visited = new boolean[V];
        Queue<Integer> queue = new LinkedList<>();
        queue.add(0);
        visited[0] = true;
        int count = 1;

        while (!queue.isEmpty()) {
            int v = queue.poll();
            for (int w : graph.adj(v)) {
                if (!visited[w]) {
                    visited[w] = true;
                    count++;
                    queue.add(w);
                }
            }
        }

        if (count != V) {
            validationMessage = "Entrada invalida: grafo desconexo ("
                    + count + " vertices alcancaveis de " + V + ")";
            return false;
        }

        validationMessage = "Entrada valida: arvore com " + V
                + " vertices e " + E + " arestas";
        return true;
    }

    public boolean isTree() {
        return treeValid;
    }

    public String getValidationMessage() {
        return validationMessage;
    }

    // ========== CENTROS ==========

    /**
     * Encontra o(s) centro(s) da arvore por remocao iterativa de folhas.
     * Retorna array com 1 ou 2 centros.
     */
    private int[] findCenters() {
        int V = graph.V();

        // Caso trivial: arvore com 1 vertice
        if (V == 1) {
            return new int[]{0};
        }

        int[] degree = new int[V];
        for (int v = 0; v < V; v++) {
            degree[v] = graph.degree(v);
        }

        // Colocar em L todos os vertices com grau 0 ou 1
        List<Integer> leaves = new ArrayList<>();
        for (int v = 0; v < V; v++) {
            if (degree[v] <= 1) {
                leaves.add(v);
            }
        }

        int processed = leaves.size();

        while (processed < V) {
            List<Integer> newLeaves = new ArrayList<>();
            for (int u : leaves) {
                for (int v : graph.adj(u)) {
                    degree[v]--;
                    if (degree[v] == 1) {
                        newLeaves.add(v);
                    }
                }
            }
            processed += newLeaves.size();
            leaves = newLeaves;
        }

        int[] result = new int[leaves.size()];
        for (int i = 0; i < leaves.size(); i++) {
            result[i] = leaves.get(i);
        }
        return result;
    }

    public int[] getCenters() {
        if (!treeValid) {
            throw new IllegalStateException("grafo nao eh uma arvore valida");
        }
        return centers;
    }

    // ========== CODIFICACAO CANONICA ==========

    /**
     * Gera a codificacao canonica da arvore.
     * - 1 centro: enraizar nele e codificar.
     * - 2 centros: enraizar em cada um, pegar a menor lexicograficamente.
     */
    private String buildCanonicalEncoding() {
        int V = graph.V();

        if (V == 1) {
            return "()";
        }

        if (centers.length == 1) {
            return encode(centers[0], -1);
        } else {
            // 2 centros: tentar os dois, usar o menor
            String enc1 = encode(centers[0], -1);
            String enc2 = encode(centers[1], -1);
            return enc1.compareTo(enc2) <= 0 ? enc1 : enc2;
        }
    }

    /**
     * Codifica recursivamente a subarvore enraizada em v,
     * ignorando o vertice parent.
     *
     * - Se v eh folha (sem filhos alem do parent): retorna "()"
     * - Senao: codifica cada filho, ordena, concatena entre parenteses
     */
    private String encode(int v, int parent) {
        List<String> childCodes = new ArrayList<>();

        for (int w : graph.adj(v)) {
            if (w != parent) {
                childCodes.add(encode(w, v));
            }
        }

        if (childCodes.isEmpty()) {
            return "()";
        }

        Collections.sort(childCodes);

        StringBuilder sb = new StringBuilder("(");
        for (String code : childCodes) {
            sb.append(code);
        }
        sb.append(")");
        return sb.toString();
    }

    public String getCanonicalEncoding() {
        if (!treeValid) {
            throw new IllegalStateException("grafo nao eh uma arvore valida");
        }
        return canonicalEncoding;
    }
}
