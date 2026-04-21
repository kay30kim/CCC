#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	
	int h[n+1];
	int w[n];
	
	int i;
	for (i = 0; i < n+1; i++) {
		scanf("%d", &h[i]);
	}
	for (i = 0; i < n; i++) {
		scanf("%d", &w[i]);
	}
//	
//	for (i = 0; i < n+1; i++) {
//		printf("%d ", h[i]);
//	}
//	printf("\n");
//	for (i = 0; i < n; i++) {
//		printf("%d ", w[i]);
//	}
//	printf("\n");
	
	double ans = 0;
	
	for (i = 0; i < n; i++) {
		double s = (h[i]+h[i+1]) * w[i] / 2.0;
//		printf("%.lf", s);
		ans += s;
//		printf("%d ", ans);
	}
//	printf("\n");
	
	printf("%.1f", ans);
}