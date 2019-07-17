#include <stdio.h>

int computeHappyNumbers(int, int);
int isHappy(int);
int ssDigits(int);

int main(void) {
	int lower1, upper1, count1, lower2, upper2, count2;

	printf("Enter 1st range: ");
	fflush(stdout);
	scanf("%d%d", &lower1, &upper1);

	printf("Enter 2nd range: ");
	fflush(stdout);
	scanf("%d%d", &lower2, &upper2);

	count1 = computeHappyNumbers(lower1, upper1);
	count2 = computeHappyNumbers(lower2, upper2);

	printf("The numbers of happy numbers in the two ranges are: %d %d\n", count1, count2);
	if (count1 > count2) {
		printf("There are more happy numbers in the first range.");
	} else if (count1 < count2) {
		printf("There are more happy numbers in the second range.");
	} else {
		printf("The number of happy numbers in both ranges are the same.");
	}

	return 0;
}

int computeHappyNumbers(int lower, int upper) {
	int count = 0;

	for (int i = lower; i <= upper; i++) {
		if (isHappy(i) == 1) {
			count++;
		}
	}
	return count;
}

int isHappy(int num) {
	while (num != 0 &&
		   num != 4 &&
		   num != 16 &&
		   num != 20 &&
		   num != 37 &&
		   num != 42 &&
		   num != 58 &&
		   num != 89 &&
		   num != 145) {
		num = ssDigits(num);
		if (num == 1) return 1;
	}
	return 0;
}

int ssDigits(int num) {
	int digit, sum = 0;

	while (num > 0) {
		digit = num % 10;
		sum += digit * digit;
		num /= 10;
	}
	return sum;
}
