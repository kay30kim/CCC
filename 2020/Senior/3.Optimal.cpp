#include <bits/stdc++.h>
#pragma GCC optimize ("O3")
using namespace std;
using ull = unsigned long long;
constexpr int INF = 0x3f3f3f3f;
constexpr ull p = 1e9 + 9;
ull p2[26];

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  string n, h;
  ull ag = 0;
  cin >> n >> h;

  p2[0] = 1;
  ull dp = 1;
  for (int i = 1; i < 26; ++i)
    p2[i] = p2[i - 1] * p;

  for (int i = 0; i < n.size(); ++i) {
    dp *= p;
    ag += p2[n[i] - 'a'];
  }

  ull hash = 0;
  ull ag2 = 0;
  for (int i = 0; i < n.size(); ++i) {
    hash = hash * p + h[i];
    ag2 = ag2 + p2[h[i] - 'a'];
  }

  unordered_set<ull> s;
  for (int i = n.size(); i < h.size(); ++i) {
    if (ag == ag2)
      s.insert(hash);

    hash = hash * p - dp * h[i - n.size()] + h[i];
    ag2 = ag2 - p2[h[i - n.size()] - 'a'] + p2[h[i] - 'a'];
  }

  if (ag == ag2)
    s.insert(hash);

  cout << s.size();
}
