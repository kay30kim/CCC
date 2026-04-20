#include<bits/stdc++.h>
using namespace std;
using ll = long long;
using pll = pair<ll, ll>;

int a[1010101];
int vis[505050];
long double d[1010101];
long double sum;

int main(){
	cin.tie(0); cout.tie(0); ios::sync_with_stdio(false);
	int n; cin >> n;
	for(int i = 1; i <= n; i++) cin >> a[i];
	if(a[1] == a[n]) return !(cout << 1);
	vis[a[n]] = n; vis[a[1]] = 1; d[1] = 1;
	for(int i = n-1; i >= 2; i--){
		if(vis[a[i]]) d[i] = d[vis[a[i]]];
		else{
			vis[a[i]] = i;
			d[i] = (sum+1)/(n-i+1);
		}
		sum += d[i];
	}
	cout << fixed << setprecision(16) << (sum+1.0)/n;
}