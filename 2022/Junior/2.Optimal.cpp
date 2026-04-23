#include <stdio.h>
int N, a, b, r = 0;
int main() {
	scanf("%d", &N);
	for(int i = 0; i < N; i++) {
		scanf("%d%d", &a, &b);
		if(5 * a - 3 * b > 40) {
			r++;
		}
	}
	printf(r == N ? "%d+" : "%d", r);
}