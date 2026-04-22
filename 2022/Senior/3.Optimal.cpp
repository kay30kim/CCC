#include<bits/stdc++.h>

#define endl "\n"
#define ends " "
#define double long double
#define sz(x) (int)(x).size()
#define all(x) (x).begin(), (x).end()

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef complex<double> cpx;

const int xw[6] = { 1,0,-1,0,0,0 };
const int yw[6] = { 0,1,0,-1,0,0 };
const int zw[6] = { 0,0,0,0,1,-1 };

const ll MOD = 1000000007;
const int INF = 0x7f7f7f7f;
const ll LINF = 0x7f7f7f7f7f7f7f7f;
const double PI = acos(-1);
const double eps = 1e-10;
// ----------------------------------------------

ll n, m, k;
ll arr[1010101];

int main() {
    cin.tie(NULL); cout.tie(NULL);
    ios_base::sync_with_stdio(false);
    // Stream Init


    cin >> n >> m >> k;
    // Input


    if (k<n || k>n * (n + 1) / 2) {
        cout << -1;
        return 0;
    }
    // Impossible


    arr[0] = 1;
    ll cnt = 0, need = k - n;

    for (int i = 1; i < n; i++) {
        if (cnt == need) {
            arr[i] = arr[i - 1];
            continue;
        }
        // Done
        
        if (i >= m) {
            if (cnt + m - 1 <= need) {
                arr[i] = arr[i - m];
                cnt += m - 1;
            }
            else {
                arr[i] = arr[i - (need - cnt) - 1];
                cnt = need;
            }
        }
        else {
            if (cnt + i <= need) {
                arr[i] = arr[i - 1] + 1;
                cnt += i;
            }
            else {
                arr[i] = arr[i - (need - cnt) - 1];
                cnt = need;
            }
        }
    }
    // Solve

    if (cnt != k - n) {
        cout << -1;
        return 0;
    }
    // Impossible

    for (int i = 0; i < n; i++)cout << arr[i] << ends;
    // Print

    return 0;
}
