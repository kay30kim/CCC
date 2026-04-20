#include <bits/stdc++.h>
#pragma GCC optimize("O3")
#pragma GCC optimize("Ofast")
#pragma GCC optimize("unroll-loops")
#define all(x) (x).begin(), (x).end()
#define fi first
#define se second

using namespace std;
using ll = long long;

int N;
vector <int> A, B;

bool is_possible() {
    vector <int> nB = {B[0]};
    for(int i = 1; i < N; i++) {
        if(B[i] != B[i-1]) nB.push_back(B[i]);
    }
    
    int i, j; i = j = 0;
    while(i < N && j < nB.size()) {
        if(A[i] == nB[j]) j++;
        i++;
    }
    return j == nB.size();
}

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    
    cin >> N;

    A.resize(N); B.resize(N);
    for(int i = 0; i < N; i++) cin >> A[i];
    for(int i = 0; i < N; i++) cin >> B[i];

    if(!is_possible()) {
        cout << "NO\n";
        return 0;
    }

    cout << "YES\n";

    int j = 0;
    vector <pair <int, int>> lswipe, rswipe;
    for(int i = 0; i < N && j < N; i++) {
        if(A[i] != B[j]) continue;

        if(j < i) lswipe.push_back({j, i});
        while(B[j] == A[i] && j < N) j++;
        if(i < j-1) rswipe.push_back({i, j-1});
    }

    reverse(all(rswipe));

    cout << lswipe.size() + rswipe.size() << "\n";
    for(int i = 0; i < lswipe.size(); i++) {
        cout << "L " << lswipe[i].fi << " " << lswipe[i].se << "\n";
    }
    for(int i = 0; i < rswipe.size(); i++) {
        cout << "R " << rswipe[i].fi << " " << rswipe[i].se << "\n";
    }
    return 0;
}