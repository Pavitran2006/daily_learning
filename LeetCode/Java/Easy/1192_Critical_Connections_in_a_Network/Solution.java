import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
    private int time = 0;

    public List<List<Integer>> criticalConnections(int n, List<List<Integer>> connections) {
        List<List<Integer>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (List<Integer> conn : connections) {
            int u = conn.get(0);
            int v = conn.get(1);
            adj.get(u).add(v);
            adj.get(v).add(u);
        }

        int[] disc = new int[n];
        int[] low = new int[n];
        Arrays.fill(disc, -1);

        List<List<Integer>> result = new ArrayList<>();

        dfs(0, -1, adj, disc, low, result);

        return result;
    }

    private void dfs(int u, int parent, List<List<Integer>> adj, int[] disc, int[] low, List<List<Integer>> result) {
        disc[u] = low[u] = ++time;

        for (int v : adj.get(u)) {
            if (v == parent) {
                continue;
            }

            if (disc[v] != -1) {
                low[u] = Math.min(low[u], disc[v]);
            } else {
                dfs(v, u, adj, disc, low, result);
                low[u] = Math.min(low[u], low[v]);

                if (low[v] > disc[u]) {
                    result.add(Arrays.asList(u, v));
                }
            }
        }
    }
}
