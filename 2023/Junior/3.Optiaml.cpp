#include <stdio.h>

const int M = 5;

int N;
int Cnt[M], Ans;

int main() {
	int i, u, chk = 0;
	char in[M + 1];

	scanf("%d", &N);
	for (i = 0; i < N; i++) {
		scanf("%s", in);
		for (u = 0; u < M; u++) Cnt[u] += (in[u] == 'Y') ? 1 : 0;
	}

	for (i = 0; i < M; i++) if (Cnt[Ans] < Cnt[i]) Ans = i;

	for (i = 0; i < M; i++) {
		if (Cnt[Ans] == Cnt[i]) {
			if (chk) printf(",");

			printf("%d", i + 1);
			chk++;
		}
	}

	return 0;
}
