#include <bits/stdc++.h>
#define int long long

using namespace std;
#define forf(i, s, e) for(int i = s; i <= e; i++)
#define endl "\n"

struct Node{
    int f, s;
    Node() : f(1e18), s(-1e18) {}
    Node(int _f, int _s) : f(_f) , s(_s) {}
    friend Node operator+(Node &a, Node &b) {
        Node ret; 
        ret.f = min(a.f, b.f);
        ret.s = max(a.s, b.s); 
        return ret; 
    }
};

struct Seg{
    Node arr[1 << 19]; 
    int sz = 1 << 18; 
    void edit(int f, Node nd) {
        for(arr[f += sz] = nd; f > 1; f >>= 1) 
            arr[f >> 1] = arr[f] + arr[f ^ 1];
    }
} tree; 

multiset <int> st[202020]; 
int N, M, Q, sum;
array <int, 2> arr[202020]; 

void edit(int i) {
    int a = 1e18, b = -1e18; 
    if(st[i].size()) a = *st[i].rbegin(); 
    if(st[i].size() >= 2) b = *prev(prev(st[i].end()));
    tree.edit(i, Node(a, b));
}

signed main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr); cout.tie(nullptr); 
    
    cin >> N >> M >> Q; 
    forf(i, 1, N) {
        int a, b; cin >> a >> b; 
        arr[i] = {a, b}; st[a].insert(b); 
    }
    
    forf(i, 1, M) edit(i), sum += *st[i].rbegin();
    cout << sum + max(0ll, tree.arr[1].s - tree.arr[1].f) << endl;
    
    while(Q--) {
        int tc, a, b; cin >> tc >> a >> b; 
        if(tc == 1) {
            int p = arr[a][0]; sum -= *st[p].rbegin() + *st[b].rbegin();
            st[p].erase(st[p].lower_bound(arr[a][1]));
            st[b].insert(arr[a][1]); arr[a][0] = b;
            edit(p), edit(b);
            sum += *st[p].rbegin() + *st[b].rbegin();
        } else {
            int n = arr[a][0]; sum -= *st[n].rbegin();
            st[n].erase(st[n].lower_bound(arr[a][1]));
            arr[a][1] = b; 
            st[n].insert(b); sum += *st[n].rbegin();
            edit(n); 
        }
        
        cout << sum + max(0ll, tree.arr[1].s - tree.arr[1].f) << endl;
    }
}