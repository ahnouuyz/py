#include<stdio.h>
#define ll long long

ll ncr(int, int);

int main () {
	int n, r;
	ll result;

	printf("Enter n and r:\n");
	scanf("%d%d", &n, &r);

	result = ncr(n, r);
	printf("%d choose %d = %lld\n", n, r, result);

	return 0;
}

ll ncr(int n, int r) {
	int i2, i3 = 1;
	ll result = 1;

	if (r < n - r) {
		r = n - r;
		printf("r reassigned to %d\n", r);
	}

	for (i2 = r + 1; i2 <= n; i2++) {
		result *= i2;
		result /= i3++;
	}

	return result;
}
