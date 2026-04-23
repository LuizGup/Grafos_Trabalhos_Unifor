import java.util.HashSet;
import java.util.Set;

public class GraphColoringDSatur {
    private final Graph graph;
    private int[] colors;           // cor de cada vertice (-1 = nao colorido)
    private int[] coloringOrder;    // ordem em que os vertices foram coloridos
    private int colorCount;         // total de cores usadas
    private boolean colored;        // flag indicando se o algoritmo ja foi executado

    private static final String[] LABELS = {
        "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA",
        "MG", "MS", "MT", "PA", "PB", "PE", "PI", "PR", "RJ", "RN",
        "RO", "RR", "RS", "SC", "SE", "SP", "TO"
    };

    public GraphColoringDSatur(Graph graph) {
        if (graph == null) {
            throw new IllegalArgumentException("graph nao pode ser nulo");
        }
        this.graph = graph;
        this.colored = false;
    }

    public Graph getGraph() {
        return graph;
    }

    /**
     * Executa o algoritmo DSatur para colorir os vertices do grafo.
     *
     * 1. Colorir o vertice de maior grau com a cor 1.
     * 2. Enquanto houver vertices nao coloridos:
     *    a. Calcular DS(v) para cada vertice nao colorido.
     *    b. Escolher o vertice com maior DS; desempate por maior grau.
     *    c. Atribuir a menor cor viavel.
     */
    public void color() {
        int V = graph.V();
        colors = new int[V];
        coloringOrder = new int[V];
        colorCount = 0;

        // inicializar todas as cores como -1 (nao colorido)
        for (int v = 0; v < V; v++) {
            colors[v] = -1;
        }

        // Passo 1: encontrar o vertice de maior grau
        int maxDegVertex = 0;
        for (int v = 1; v < V; v++) {
            if (graph.degree(v) > graph.degree(maxDegVertex)) {
                maxDegVertex = v;
            }
        }

        // colorir o vertice de maior grau com a cor 1
        colors[maxDegVertex] = 1;
        colorCount = 1;
        coloringOrder[0] = maxDegVertex;

        // Passo 2: colorir os demais vertices
        for (int step = 1; step < V; step++) {
            // encontrar o vertice nao colorido com maior DS;
            // desempate por maior grau
            int chosen = -1;
            int maxDS = -1;
            int maxDeg = -1;

            for (int v = 0; v < V; v++) {
                if (colors[v] != -1) continue; // ja colorido

                int ds = saturationDegree(v);
                int deg = graph.degree(v);

                if (ds > maxDS || (ds == maxDS && deg > maxDeg)) {
                    maxDS = ds;
                    maxDeg = deg;
                    chosen = v;
                }
            }

            // atribuir a menor cor viavel ao vertice escolhido
            int k = smallestAvailableColor(chosen);
            colors[chosen] = k;
            if (k > colorCount) {
                colorCount = k;
            }
            coloringOrder[step] = chosen;
        }

        colored = true;
    }

    /**
     * Calcula o grau de saturacao DS(v): numero de cores distintas
     * ja presentes na vizinhanca de v.
     */
    private int saturationDegree(int v) {
        Set<Integer> neighborColors = new HashSet<>();
        for (int w : graph.adj(v)) {
            if (colors[w] != -1) {
                neighborColors.add(colors[w]);
            }
        }
        return neighborColors.size();
    }

    /**
     * Encontra a menor cor k >= 1 que nao conflita com nenhum
     * vizinho ja colorido de v.
     */
    private int smallestAvailableColor(int v) {
        Set<Integer> usedColors = new HashSet<>();
        for (int w : graph.adj(v)) {
            if (colors[w] != -1) {
                usedColors.add(colors[w]);
            }
        }
        int k = 1;
        while (usedColors.contains(k)) {
            k++;
        }
        return k;
    }

    /**
     * Retorna a cor atribuida ao vertice.
     */
    public int getColor(int vertex) {
        if (!colored) {
            throw new IllegalStateException("execute color() antes de consultar cores");
        }
        return colors[vertex];
    }

    /**
     * Retorna o total de cores utilizadas na coloracao.
     */
    public int getColorCount() {
        if (!colored) {
            throw new IllegalStateException("execute color() antes de consultar o total de cores");
        }
        return colorCount;
    }

    /**
     * Retorna uma copia do array com a ordem em que os vertices
     * foram coloridos.
     */
    public int[] getColoringOrder() {
        if (!colored) {
            throw new IllegalStateException("execute color() antes de consultar a ordem");
        }
        int[] copy = new int[coloringOrder.length];
        System.arraycopy(coloringOrder, 0, copy, 0, coloringOrder.length);
        return copy;
    }

    /**
     * Verifica se a coloracao produzida eh valida:
     * para cada aresta (v, w), as cores de v e w devem ser diferentes.
     */
    public boolean isValidColoring() {
        if (!colored) {
            throw new IllegalStateException("execute color() antes de validar");
        }
        int V = graph.V();
        for (int v = 0; v < V; v++) {
            for (int w : graph.adj(v)) {
                if (colors[v] == colors[w]) {
                    return false;
                }
            }
        }
        return true;
    }

    /**
     * Retorna o rotulo (sigla do estado) correspondente ao vertice.
     * Se o grafo nao tiver 27 vertices, retorna apenas o numero.
     */
    public String getLabel(int vertex) {
        if (vertex >= 0 && vertex < LABELS.length && graph.V() == LABELS.length) {
            return LABELS[vertex];
        }
        return String.valueOf(vertex);
    }
}
