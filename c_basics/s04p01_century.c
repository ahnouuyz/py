#include <stdio.h>
#include <math.h.>

int printCentury(int);
char * printOrdinal(int);

int main(void) {
	char *ordinal;
	int century, year;

	printf("Enter year: ");
	fflush(stdout);
	scanf("%d", &year);

	century = printCentury(year);
	ordinal = printOrdinal(year);

	printf("The year %d falls in the %d%s century.", year, century, ordinal);
	return 0;
}

int printCentury(int year) {
	return ceil(year / 100) + 1;
}

char * printOrdinal(int year) {
	int cent, last_2, last_1;

	cent = printCentury(year);
	last_2 = cent % 100;
	last_1 = cent % 10;

	if (last_2 == 13 || last_2 == 12 || last_2 == 11) {
		return "th";
	} else {
		switch (last_1 % 10) {
			case 1:
				return "st";
			case 2:
				return "nd";
			case 3:
				return "rd";
			default:
				return "th";
		}
	}
}
