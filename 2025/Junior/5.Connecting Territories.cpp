#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int R, C;
    int M;
    cin >> R >> C >> M;

    const long long INF = LLONG_MAX / 4;

    vector<long long> dp_prev(C, INF), dp_curr(C, INF);

    int val = 1;

    // 첫 번째 행
    for (int j = 0; j < C; j++) {
        dp_prev[j] = val;
        val++;
        if (val > M) val = 1;
    }

    // 나머지 행
    for (int i = 1; i < R; i++) {
        // 첫 열
        dp_curr[0] = min(dp_prev[0], dp_prev[1]) + val;
        val++;
        if (val > M) val = 1;

        // 중간 열
        for (int j = 1; j < C - 1; j++) {
            dp_curr[j] = min({dp_prev[j - 1], dp_prev[j], dp_prev[j + 1]}) + val;
            val++;
            if (val > M) val = 1;
        }

        // 마지막 열
        dp_curr[C - 1] =
            min(dp_prev[C - 2], dp_prev[C - 1]) + val;
        val++;
        if (val > M) val = 1;

        dp_prev.swap(dp_curr);
    }

    cout << *min_element(dp_prev.begin(), dp_prev.end()) << "\n";
    return 0;
}
