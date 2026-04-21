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

	ll mx = 0;
	vector<pair<ll, pll>> vec;
	int n = getu();
	for (int i = 0; i < n; i++) {
		ll a, b, c;
        a = getu();
        b = getu();
        c = getu();
		vec.emplace_back(a, pll(b, c));
		mx = max(mx, a);
	}

	auto solve = [&](ll pos) {
		ll ret = 0;
		for (const auto &[p, wd] : vec) ret += max(0LL, llabs(pos - p) - wd.second) * wd.first;
		return ret;
	};

	ll l = 0, r = mx;
	while (l < r) {
		ll mid = (l + r) >> 1;
		ll p1 = solve(mid - 1), p2 = solve(mid), p3 = solve(mid + 1);
		if (p2 <= min(p1, p3)) break;
		if (p1 >= p2 && p2 >= p3) l = mid + 1;
		else r = mid - 1;
	}

	cout << solve((l + r) >> 1);
}
