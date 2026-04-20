#include <iostream>
using namespace std;
typedef long long ll;

ll plen, period, idx;
string s;
pair<char, ll> P[100001];
char c; ll val;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> s >> idx;
    for (auto &l:s) {
        if ('a' <= l && l <= 'z') {
            P[plen++] = make_pair(c, val);
            period += val;
            c = l, val = 0;
        }
        else val = val * 10 + (l - '0');
    }
    P[plen++] = make_pair(c, val);
    period += val;

    idx %= period;
    for (int i = 0; i < plen; i++) {
        idx -= P[i].second;
        if (idx < 0) cout << P[i].first, exit(0);
    }
}