#include <stdio.h>
#include <math.h>

double computeFee(int, int, int);
int timeDeltaMinutes(int, int);

int main(void) {
	double fee;
	int day, timeIn, timeOut;

	printf("Enter day: ");
	fflush(stdout);
	scanf("%d", &day);

	printf("Enter time-in: ");
	fflush(stdout);
	scanf("%d", &timeIn);

	printf("Enter time-out: ");
	fflush(stdout);
	scanf("%d", &timeOut);

	fee = computeFee(day, timeIn, timeOut);

	printf("Parking fee is $%.2f.", fee);
	return 0;
}

double computeFee(int day, int timeIn, int timeOut) {
	double fee;
	int block1 = 0, block2 = 0, block3 = 0, dur;

	if (timeOut - timeIn <= 10) return 0.0;

	if (day == 7) {
		fee = 5.0;
	} else {
		if (timeOut > 1800) {
			block3 = 1;
			if (timeIn < 700) {
				block2 = 22;
				block1 = ceil(timeDeltaMinutes(timeIn, 700) / 60.0);
			} else {
				block2 = ceil(timeDeltaMinutes(timeIn, 1800) / 30.0);
			}
		} else if (timeOut > 700) {
			block2 = ceil(timeDeltaMinutes(700, timeOut) / 30.0);
			if (timeIn < 700) {
				block1 = ceil(timeDeltaMinutes(timeIn, 700) / 60.0);
			}
		} else {
			block1 = ceil(timeDeltaMinutes(timeIn, timeOut) / 60.0);
		}

		dur = timeDeltaMinutes(timeIn, timeOut);

		if (day == 6) {
			fee = block1 * 2.5 + block2 * 1.5 + block3 * 7.0;
			if (dur > 600) fee *= 1.2;
		} else {
			fee = block1 * 2.0 + block2 * 1.2 + block3 * 5.0;
			if (dur > 600) fee *= 1.1;
		}
	}

	if (timeOut > 2200) fee += 3.0;
	return fee;
}

int timeDeltaMinutes(int t0, int t1) {
	int h0, h1, m0, m1;

	h0 = t0 / 100;
	h1 = t1 / 100;
	m0 = t0 % 100;
	m1 = t1 % 100;

	return (h1 - h0) * 60 + (m1 - m0);
}
