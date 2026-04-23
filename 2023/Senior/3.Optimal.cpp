#include <bits/stdc++.h>
using namespace std;
const int N = 2005;
int n, m, r, c;
char ans[N][N];
void print() {
	for(int i = 0; i < n; i ++) {
    	for(int j = 0; j < m; j ++) {
    		cout << ans[i][j];
    	}
    	cout << "\n";
    }
}
int main() {
    cin.tie(0)->sync_with_stdio(0);
    cin >> n >> m >> r >> c;
    for(int i = 0; i < n; i ++) {
    	for(int j = 0; j < m; j ++) {
    		ans[i][j] = 'b'+(i+j)%25;
    	}
    }
    if((r == n) ^ (c == m)) {
    	for(int i = 0; i < n; i ++) {
	    	for(int j = 0; j < m; j ++) {
	    		ans[i][j] = 'b';
	    	}
	    }
    	if(r == n && (m-c)%2 <= m%2) {
    		if((m-c)%2) {
    			ans[0][m/2] = 'a';
    			c ++;
    		}
    		for(int i = 0; i*2 < m-c; i ++) {
    			ans[0][i] = 'a';
    			ans[0][m-i-1] = 'a';
    		}
    		print();
    	} else if(c == m && (n-r)%2 <= n%2) {
    		if((n-r)%2) {
    			ans[n/2][0] = 'a';
    			r ++;
    		}
    		for(int i = 0; i*2 < n-r; i ++) {
    			ans[i][0] = 'a';
    			ans[n-i-1][0] = 'a';
    		}
    		print();
    	} else {
    		cout << "IMPOSSIBLE";
    	}
    	return 0;
    }
    for(int i = 0; i < r; i ++) {
    	for(int j = 0; j < m; j ++) {
    		ans[i][j] = 'a';
    	}
    }
    for(int i = 0; i < n; i ++) {
    	for(int j = 0; j < c; j ++) {
    		ans[i][j] = 'a';
    	}
    }
    print();
}