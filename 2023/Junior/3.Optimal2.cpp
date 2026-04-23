#include <stdio.h>
#define max(a, b) (a > b ? a : b)
int N, A[5] = { 0, }, a = 0, b = 0;
char S[6];
int main() {
	scanf("%d", &N);
	while(N--) {
		scanf("%s", S);
		for(int i = 0; i < 5; i++) {
			A[i] += (S[i] == 'Y' ? 1 : 0);
			a = max(a, A[i]);
		}
	}
	for(int i = 0; i < 5; i++) {
		if(A[i] == a) {
			printf(b == 1 ? ",%d" : "%d", i + 1);
			b = 1;
		}
	}
}