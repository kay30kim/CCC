#pragma GCC optimize("Ofast")

#include <bits/stdc++.h>
using namespace std;
#define tii tuple<int, int, int, int>
#define all(x) (x).begin(), (x).end()
#define ll long long

int n, m;
vector<tii> edges;

vector<pair<int, int>> adj[2001];
bool visited[2001];
ll dist[2001];
ll ans = 0;

ll dijkstra(int a, int b) { // a -> b
	priority_queue<pair<ll, int>> pq;
	memset(visited, 0, 2001);
	memset(dist, 0x7f, 2001 * 8);
	pq.push({0, a});
	dist[a] = 0;
	while (!pq.empty()) {
		int x = pq.top().second;
		pq.pop();
		if (visited[x]) continue;
		visited[x] = true;
		if (x == b) return dist[b];
		for (auto p : adj[x]) {
			int y = p.first;
			int z = p.second;
			if (dist[y] > dist[x] + z) {
				dist[y] = dist[x] + z;
				pq.push({-dist[y], y});
			}
		}
	}
	return dist[b];
}

int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int u, v, l, c;
		cin >> u >> v >> l >> c;
		edges.push_back({l, c, u, v});
	}
	sort(all(edges));
	for (auto &e : edges) {
		ll bruh = dijkstra(get<2>(e), get<3>(e));
		if (bruh > get<0>(e)) {
			adj[get<2>(e)].push_back({get<3>(e), get<0>(e)});
			adj[get<3>(e)].push_back({get<2>(e), get<0>(e)});
			ans += get<1>(e);
		}
	}
	cout << ans << '\n';
	return 0;
}