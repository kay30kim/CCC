#include <bits/stdc++.h>
using namespace std;

int n;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;
    int arr[2][n];
    int count = 0;
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }
    for (int i = 0; i < 2; i++) {
        for (int j = 0; j < n; j++) {
            if (arr[i][j] == 1) {
                count += 3;
                if(j < n - 1) {
                    if (arr[i][j+1] == 1) {
                        count -= 2;
                    }
                }
                if (i == 0 && j % 2 == 0) {
                    if (arr[i+1][j] == 1) {
                        count -= 2;
                    }
                }
            }
        }
    }
    cout << count;
    return 0;
}
