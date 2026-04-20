#include <bits/stdc++.h>
#define sz(v) ((int)(v).size())
#define all(v) (v).begin(), (v).end()
#define cr(v, n) (v).clear(), (v).resize(n);
using namespace std;
using lint = long long;
using pi = array<lint, 2>;
const int MAXN = 200005;

vector<pi> gph[MAXN];

vector<lint> dijkstra(int s, int n) {
	priority_queue<pi, vector<pi>, greater<pi>> pq;
	vector<lint> dist(n, 1e18);
	auto enq = [&](int x, lint v) {
		if (dist[x] > v) {
			dist[x] = v;
			pq.push({v, x});
		}
	};
	enq(s, 0);
	while (sz(pq)) {
		auto x = pq.top();
		pq.pop();
		if (dist[x[1]] != x[0])
			continue;
		for (auto &[w, y] : gph[x[1]])
			enq(y, w + x[0]);
	}
	return dist;
}

void add_edge(int s, int e, lint x) { gph[s].push_back({x, e}); }

int main() {
	ios::sync_with_stdio(false);
	cin.tie(0);
	cout.tie(0);
	int n, m;
	cin >> n >> m;
	vector<vector<pi>> gph(n);
	for (int i = 0; i < m; i++) {
		int u, v, w;
		cin >> u >> v >> w;
		u--;
		v--;
		gph[u].push_back({w, i});
		gph[v].push_back({w, i});
	}
	for (int i = 0; i < n; i++) {
		sort(all(gph[i]));
		for (int j = 1; j < sz(gph[i]); j++) {
			auto [l1, v1] = gph[i][j - 1];
			auto [l2, v2] = gph[i][j];
			add_edge(v1, v2, l2 - l1);
			add_edge(v2, v1, l2 - l1);
		}
		if (i == 0) {
			for (auto &[_, j] : gph[i])
				add_edge(m, j, _);
		}
		if (i == n - 1) {
			for (auto &[_, j] : gph[i]) {
				add_edge(j, m + 1, 0);
			}
		}
	}
	cout << dijkstra(m, m + 2)[m + 1] << "\n";
}
