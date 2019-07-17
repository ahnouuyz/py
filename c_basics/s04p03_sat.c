#include <stdio.h>

int compute_percentile(int, int, int);
float compute_iqscore(int, int);

int main(void) {
	int verbal, math, writing, percentile;
	float iqscore;

	printf("Enter scores: ");
	fflush(stdout);
	scanf("%d%d%d", &verbal, &math, &writing);

	percentile = compute_percentile(verbal, math, writing);
	iqscore = compute_iqscore(verbal, math);

	printf("The SAT score is in the %d percentile.\n", percentile);
	printf("The IQ score is %.2f", iqscore);
	if ((verbal > 600 && math > 600 && writing > 600) || iqscore >= 120) {
		printf("\nWow, this is amazing!");
	}
	return 0;
}

int compute_percentile(verbal, math, writing) {
	int total = verbal + math + writing;

	if (total >= 2200) {
		return 99;
	} else if (total >= 2000) {
		return 95;
	} else if (total >= 1500) {
		return 50;
	} else {
		return 10;
	}
}

float compute_iqscore(verbal, math) {
	return (0.095 * math) + (0.003 * verbal) + 50.241;
}
