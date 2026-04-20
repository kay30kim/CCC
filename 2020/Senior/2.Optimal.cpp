#include <bits/stdc++.h>
using namespace std;
using ll = int;

short p[1000005][29];
char sz[1000005];
ll a[1005][1005];
bool v[1005][1005];

char buf[8000100];
inline int ri()
{
    static int i = 0;
    int x = buf[i++] - '0';
    while (buf[i] >= '0')
        x = x * 10 + buf[i++] - '0';
    return ++i, x;
}

int main()
{
    fread(buf, 1, sizeof buf, stdin);
	ll i, j;
	for (i = 1; i <= 1000; i++)
		for (j = i * i; j <= 1000 * i; j += i)
    		p[j][sz[j]++] = i;
	
	ll n = ri(), m = ri();
	for (i = 1; i <= n; i++)
		for (j = 1; j <= m; j++)
			a[i][j] = ri();
	queue<pair<ll, ll>> q;
	q.push({1, 1});
	v[1][1] = true;
	while (q.size())
	{
		auto [y, x] = q.front();
		q.pop();

		if (y == n && x == m)
			return cout << "yes\n", 0;

		for (i = 0; i < sz[a[y][x]]; i++)
		{
			ll yy = p[a[y][x]][i];
			ll xx = a[y][x] / yy;
			if (!v[yy][xx])
			{
				v[yy][xx] = true;
				q.push({yy, xx});
			}
			swap(yy, xx);
			if (!v[yy][xx])
			{
				v[yy][xx] = true;
				q.push({yy, xx});
			}
		}
	}
	cout << "no\n";
}