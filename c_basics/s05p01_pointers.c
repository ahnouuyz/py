#include <stdio.h>

int main(void) {
	int a, *a_ptr;
	float b, *b_ptr;

	printf("Enter an integer: ");
	fflush(stdout);
	scanf("%d", a_ptr);
	printf("Enter a real number: ");
	fflush(stdout);
	scanf("%f", &b);

	a = *a_ptr;

	while (a < b * b) {
		a *= b;
	}

	printf("Values entered are %d and %.2f\n", *a_ptr, b);
	printf("Final value of a = %d", a);

	return 0;
}
