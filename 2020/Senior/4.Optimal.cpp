#include <bits/stdc++.h>
#define N 2000005
using namespace std;
int n,ans=1e9,sa[N],sb[N],sc[N];char s[N];
#define A(x,y) (sa[y]-sa[x-1])
#define B(x,y) (sb[y]-sb[x-1])
#define C(x,y) (sc[y]-sc[x-1])
int main() {
	scanf("%s",s+1);
	n=strlen(s+1);
	for(int i=1;i<=n;++i) {
		sa[i]=sa[i-1]+(s[i]=='A');
		sb[i]=sb[i-1]+(s[i]=='B');
		sc[i]=sc[i-1]+(s[i]=='C');
	}
	for(int i=1;i<=n;++i) {
		sa[i+n]=sa[i+n-1]+(s[i]=='A');
		sb[i+n]=sb[i+n-1]+(s[i]=='B');
		sc[i+n]=sc[i+n-1]+(s[i]=='C');
	}
	for(int i=1;i<=n;++i) {
		int s1=B(i,i+sa[n]-1),s2=C(i,i+sa[n]-1),s3=A(i+sa[n],i+sa[n]+sb[n]-1),s4=C(i+sa[n],i+sa[n]+sb[n]-1);
		ans=min(ans,s1+s2+s4+(s3>s1?s3-s1:0));
		s1=B(i,i+sa[n]-1),s2=C(i,i+sa[n]-1),s3=A(i+sa[n],i+sa[n]+sc[n]-1),s4=B(i+sa[n],i+sa[n]+sc[n]-1);
		ans=min(ans,s1+s2+s4+(s3>s2?s3-s2:0));
	}
	printf("%d\n",ans);
	return 0;
}