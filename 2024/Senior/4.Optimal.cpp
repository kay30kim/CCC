#include <bits/stdc++.h>
using namespace std;

int n, m;
vector<pair<int, int>> adj[200005];
bool vis[200005];
string ans;

void dfs(int u, bool red=1) {
    vis[u]=1;
    for (const auto &i : adj[u]) {
        if (vis[i.first]) continue;
        ans[i.second]=red?'B':'R';
        dfs(i.first, !red);
    }
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
    ans.resize(m, 'G');
    for (int i = 0; i < m; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back({v,i});
        adj[v].push_back({u,i});
    }
    for (int i = 1; i <= n; i++) if (!vis[i]) dfs(i);
    cout << ans << '\n';
    return 0;
}