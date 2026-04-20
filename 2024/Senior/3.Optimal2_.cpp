#include <algorithm>
#include <iostream>
#include <tuple>
#include <vector>

using namespace std;

bool is_subsequence(vector<int> &a, vector<int> &b){
    int n = (int)a.size(), m = (int)b.size();
    int j = 0;
    for(int i = 0; i < n; ++i){
        if(j < m && b[j] == a[i]){
            ++j;
        }
    }
    return j == m;
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int n;
    cin >> n;
    vector<int> a(n), b(n);
    for(int i = 0; i < n; ++i){
        cin >> a[i];
    }
    for(int i = 0; i < n; ++i){
        cin >> b[i];
    }
    vector<int> c = a, d = b;
    c.erase(unique(c.begin(), c.end()), c.end());
    d.erase(unique(d.begin(), d.end()), d.end());
    if(!is_subsequence(c, d)){
        cout << "NO\n";
        return 0;
    }
    vector<tuple<char, int, int>> right_only, left_only, left_and_right;
    int j = 0;
    int k = 0, l = 0;
    for(int i = 0; i < (int)c.size(); ++i){
        while(k < n && a[k] != c[i]){
            ++k;
        }
        if(j < (int)d.size() && c[i] == d[j]){
            int r = l;
            while(r < n && b[l] == b[r]){
                ++r;
            }
            --r;
            if(r > k && l >= k){
                right_only.push_back(make_tuple('R', k, r));
            }else if(l < k && r <= k){
                left_only.push_back(make_tuple('L', l, k));
            }else{
                if(l < k){
                    left_and_right.push_back(make_tuple('L', l, k));
                }
                if(r > k){
                    left_and_right.push_back(make_tuple('R', k, r));
                }
            }
            ++j;
            while(l < n && b[l] != d[j]){
                ++l;
            }
        }
    }
    reverse(right_only.begin(), right_only.end());
    cout << "YES\n" << right_only.size() + left_only.size() + left_and_right.size() << "\n";
    for(tuple<char, int, int> &t : right_only){
        char x;
        int y, z;
        tie(x, y, z) = t;
        cout << x << " " << y << " " << z << "\n";
    }
    for(tuple<char, int, int> &t : left_only){
        char x;
        int y, z;
        tie(x, y, z) = t;
        cout << x << " " << y << " " << z << "\n";
    }
    for(tuple<char, int, int> &t : left_and_right){
        char x;
        int y, z;
        tie(x, y, z) = t;
        cout << x << " " << y << " " << z << "\n";
    }
    return 0;
}