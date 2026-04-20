#include <iostream>
using namespace std;

int N;
int val1, val2, mx;
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> N;
    for (int i = 0; i < N; i++) {
        char c; cin >> c;
        if (c == 'S') val1++, val2++;
        else val2 = val1 + 1, val1 = 0;
        mx = max(mx, max(val1, val2));
    }
    if (N == val1) cout << N - 1;
    else cout << mx;
}