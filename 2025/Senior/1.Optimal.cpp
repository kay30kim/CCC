#include <stdio.h>

int main() {
	int a, b, c, d, A, B;

	scanf("%d%d%d%d", &a, &b, &c, &d);
	A = ((a > c) ? a : c) + (b + d), B = (a + c) + ((b > d) ? b : d);
	printf("%d", ((A < B) ? A : B) * 2);

	return 0;
}
