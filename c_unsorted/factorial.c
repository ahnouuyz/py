#include<stdio.h>
#include<math.h>

long fac(unsigned long n);

int main(void) {
	for (long i = 0; i < 9; i++) {
		printf("%ld --- %ld\n", i, fac(i));
	}
	return 0;
}

long fac(unsigned long n) {
	return lround(exp(lgamma(n + 1)));
}
