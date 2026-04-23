#include <stdio.h>
int T, A[256], C[6] = { 1500, 6000, 15500, 40000, 75000, 125000 }, a = 0;
char S[10], B[7] = "PMSCTH";
int main() {
	scanf("%d", &T);
	for(int i = 0; i < 6; i++) {
		A[B[i]] = C[i];
	}
	while(T--) {
		scanf("%s", S);
		a += A[S[0]];
	}
	printf("%d", a);
}