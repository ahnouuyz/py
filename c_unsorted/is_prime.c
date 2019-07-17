#include<stdio.h>
#include<math.h>

int is_prime(int);

int main () {
	int number, result;

	printf("Enter a number: ");
	scanf("%d", &number);

	result = is_prime(number);
	if (result == 1) {
		printf("%d is a prime.\n", number);
	} else {
		printf("%d is not a prime.\n", number);
	}

	return 0;
}

int is_prime(int number) {
	int i2;

	if (number == 2) {
		return 1;
	} else if (number > 2) {
		if (number % 2 == 0)
			return 0;
		for (i2 = 3; i2 < (int)sqrt(number) + 1; i2 += 2) {
			if (number % i2 == 0)
				return 0;
		}
		return 1;
	} else {
		return 0;
	}
}
