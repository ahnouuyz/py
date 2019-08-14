#include<stdio.h>
#include<math.h>

long fib(unsigned long n);

int main(void) {
	for (long i = 0; i < 9; i++) {
		printf("%ld --- %ld\n", i, fib(i));
	}
	return 0;
}

long fib(unsigned long n) {
	return lround((pow(0.5 + 0.5 * sqrt(5.0), n) -
				   pow(0.5 - 0.5 * sqrt(5.0), n)) /
			      sqrt(5.0));
}
