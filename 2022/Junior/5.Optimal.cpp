#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <list>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <cmath>
#include <bitset>
#include <unordered_set>
#include <climits>
#include <complex>
#include <cassert>
#include <numeric>
#include <random>
using namespace std;
typedef long long ll;

const int MAX_N=1005;
const ll INF=1e15;
const int MOD=1000000;

typedef struct P{
    int x, y;
}P;

int n,t,a,b;
vector<P> tree;

int check(int m){
    int len=tree.size();
    for(int i=0;i<len;i++){
        for(int j=i+1;j<len;j++){
            int sx, sy,ex,ey;
            int x1=tree[i].x, y1=tree[i].y, x2=tree[j].x, y2=tree[j].y;
            if(x1==x2){
                sx=x1+1; sy=min(y1, y2)+1;
            }
            else if(y1==y2){
                sx=min(x1, x2)+1; sy=y1+1;
            }
            else if(x1<x2){
                sx=x1+1; sy=y2+(y1<y2?-m:1);
            }
            else{
                sx=x2+1; sy=y1+(y1<y2?1:-m);
            }
            ex=sx+m-1, ey=sy+m-1;
            if(sx<1 || sy<1 || ex>n || ey>n){continue;}
            int p = 1;
            for(auto [tx, ty]:tree){
                if(sx <= tx && tx <= ex && sy <= ty && ty <= ey){
                    p = 0; break;
                }
            }
            if(p) return 1;
        }
    }

    return 0;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin>>n>>t;
    for(int i=0;i<t;i++){
        cin>>a>>b; tree.push_back({a,b});
    }
    tree.push_back({0,0});
    tree.push_back({n+1, n+1});
    int low=0, high=n, ans=0;
    while (low <= high) {
        int mid=(low+high)/2;
        if (check(mid)) {
            ans = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    cout<<ans<<"\n";
    return 0;
}