#include <iostream>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	string s;

	for (char c; cin >> c;) {
		if (c == '+' || c == '-') {
			int num;
			cin >> num;

			cout << s << ' ' << (c == '+' ? "tighten" : "loosen") << ' ' << num << '\n';
			s.clear();
		}
		else
			s += c;
	}
}