#include<bits/stdc++.h>

int main() {
	using namespace std;
	cin.tie(nullptr)->sync_with_stdio(false);
	int N, M; cin >> N >> M;

	using i64 = int64_t;

	vector<tuple<i64, i64, int, int>> edges;
	edges.reserve(M);
	for (int i = 0; i < M; ++i) {
		int a, b; i64 l, c; cin >> a >> b >> l >> c;
		--a, --b;
		edges.push_back({l, c, a, b});
	}

	const i64 INF = 1e18;

	sort(edges.begin(), edges.end());

	i64 ans = 0;
	vector<vector<pair<i64, int>>> adj(N);
	for (auto [len, cost, a, b] : edges) {
		priority_queue<pair<i64, int>> que;
		vector<i64> min_dist(N, INF);
		min_dist[a] = 0;
		que.push({0, a});

		while (!que.empty()) {
			auto [cur_len, cur] = que.top();
			cur_len = -cur_len;
			que.pop();

			if (cur_len != min_dist[cur]) continue;

			for (auto [nxt, nxt_len] : adj[cur]) {
				if (cur_len + nxt_len < min_dist[nxt]) {
					min_dist[nxt] = cur_len + nxt_len;
					que.push({-min_dist[nxt], nxt});
				}
			}
		}

		if (min_dist[b] > len) {
			ans += cost;
			adj[a].push_back({b, len});
			adj[b].push_back({a, len});
		}
	}

	cout << ans << '\n';
}
