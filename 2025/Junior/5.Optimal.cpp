#pragma GCC optimize("O3")
#pragma GCC optimize("unroll-loops")
#include <iostream>
using namespace std;

unsigned int R, C, val, K, ans = 4000000077LL;
unsigned int A[20002], B[20002];

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> R >> C >> K;
    A[0] = A[C + 1] = B[0] = B[C + 1] = 2000000007;
    for (int i = 0; i < R; i++) {
        for (int c = 1; c <= C; c++) {
            val++;
            if (val > K) val -= K;
            B[c] = min(A[c - 1], min(A[c], A[c + 1])) + val;
        }
        swap(A, B);
    }

    for (int c = 1; c <= C; c++) ans = min(ans, A[c]);
    cout << ans;
}