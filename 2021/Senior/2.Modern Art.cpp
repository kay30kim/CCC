#include <bits/stdc++.h>

#define all(v) v.begin(), v.end()

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;
typedef pair<ld, ld> pld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<ld> vld;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
typedef vector<pld> vpld;
typedef unordered_map<int, int> mpii;

#include <sys/stat.h>
#include <sys/mman.h>
signed I[36];char*J=(char*)mmap(0,I[12],1,2,0,fstat(0,(struct stat*)I));
int getu(){int x=0;do x=x*10+*J-'0';while(*++J>='0');++J;return x;}
int geti(){bool e=*J=='-';J+=e;return(e?-1:1)*getu();}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	cout.tie(nullptr);

	ll m, n, k;
    m = getu();
    n = getu();
    k = getu();
	vl R(m + 1), C(n + 1);
	while (k--) {
		char c = *J; ++J; ++J;
		int a = getu();
		if (c == 'R') R[a]++, R[a] %= 2;
		else C[a]++, C[a] %= 2;
	}

	ll R_c = reduce(all(R)), C_c = reduce(all(C));
	cout << R_c * n + C_c * m - 2 * R_c * C_c;
}
