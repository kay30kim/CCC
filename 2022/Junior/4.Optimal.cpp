#include <iostream>
#include <vector>
#include <map>
#include <utility>
#include <unordered_map>

using namespace std;

int main() {
      cin.tie(0)->sync_with_stdio(0);
      int n;
      cin >> n;
      vector<pair<string,string>> t;
      t.reserve(n);
      for (int i = 0; i < n; i++) {
            string a, b;
            cin >> a >> b;
            t.push_back({a, b});
      }
      int y;
      cin >> y;

      vector<pair<string,string>> s;
      s.reserve(y);
      for (int i = 0; i < y; i++) {
            string a, b;
            cin >> a >> b;
            s.push_back({a, b});
      }
      int G;
      cin >> G;

      unordered_map<string, int> grp;
      grp.reserve(G * 3 * 2);

      for (int i = 0; i < G; i++) {
            string s1, s2, s3;
            cin >> s1 >> s2 >> s3;
            grp[s1] = i;
            grp[s2] = i;
            grp[s3] = i;
      }

      int check = 0;

      for (auto &p : t) {
            if (grp[p.first] != grp[p.second]) check++;
      }
      for (auto &p : s) {
            if (grp[p.first] == grp[p.second]) check++;
      }

      cout << check;
      return 0;
}