#include <iostream>
#include <algorithm>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef long double ld;

const int MAXN=1e5+1;
int N;
ii A[MAXN];
ld ans = 0;

int main(int argc, const char * argv[]) {
    ios_base::sync_with_stdio(false); cin.tie(0);
    cin >> N;
    for(int i=0; i<N; i++) cin >> A[i].first >> A[i].second;
    sort(A,A+N);
    for(int i=0; i<N-1; i++){
        ans = max(ans,(ld)(abs(A[i+1].second-A[i].second))/(A[i+1].first-A[i].first));
    }
    cout << ans << "\n";
}
