#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<char> weathers(n);

    for (int i = 0; i < n; i++) {
        cin >> weathers[i];
    }

    // Python: if 'P' not in weathers
    bool hasP = false;
    for (char c : weathers) {
        if (c == 'P') {
            hasP = true;
            break;
        }
    }
    if (!hasP) {
        cout << n - 1;
        return 0;
    }

    int left = 0, rain = 0, ans = 0;

    for (int right = 0; right < n; right++) {
        if (weathers[right] == 'P')
            rain++;

        while (rain > 1) {
            if (weathers[left] == 'P')
                rain--;
            left++;
        }

        ans = max(ans, right - left + 1);
    }

    cout << ans;
    return 0;
}
