#include <stdio.h>

int countWinners(int, int, int);
int hasDigit(int, int);

int main(void) {
	int factor, must_have, n, win_count;

	printf("Enter factor-digit: ");
	fflush(stdout);
	scanf("%d", &factor);

	printf("Enter must-have-digit: ");
	fflush(stdout);
	scanf("%d", &must_have);

	printf("Enter number of participants: ");
	fflush(stdout);
	scanf("%d", &n);

	win_count = countWinners(factor, must_have, n);

	printf("Number of winners: %d", win_count);
	return 0;
}

int countWinners(int factor, int must_have, int n) {
	int count = 0;

	for (int i = 1; i <= n; i++) {
		if (i % factor == 0 && hasDigit(i, must_have) == 1) {
			count++;
		}
	}
	return count;
}

int hasDigit(int i, int must_have) {
	while (i > 0) {
		if (i % 10 == must_have) {
			return 1;
		}
		i /= 10;
	}
	return 0;
}
