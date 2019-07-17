#include <stdio.h>

int luhnah(int);
char * issued(int);

int main(void) {
	char *branch;
	int uCardNo, checkNum;

	printf("Enter uCard Number: ");
	fflush(stdout);
	scanf("%d", &uCardNo);

	checkNum = luhnah(uCardNo);
	printf("The check number is %d\n", checkNum);

	if (checkNum % 7 == 0) {
		printf("Valid\n");
		branch = issued(uCardNo);
		printf("Issued by %s", branch);
	} else {
		printf("Invalid");
	}
	return 0;
}

int luhnah(int uCardNo) {
	int sum = 0, even = 0;

	while (uCardNo > 0) {
		if (even == 1) {
			sum += ((uCardNo % 10) * 2) % 9;
			even = 0;
		} else {
			sum += uCardNo % 10;
			even = 1;
		}
		uCardNo /= 10;
	}
	return sum;
}

char * issued(int uCardNo) {
	while (uCardNo >= 100) {
		uCardNo /= 10;
	}
	if (uCardNo >= 31 && uCardNo <= 35) {
		return "East branch";
	} else if (uCardNo >= 51 && uCardNo <= 55) {
		return "West branch";
	} else {
		return "Central branch";
	}
}
