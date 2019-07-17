#include <stdio.h>

int min_unused_area(int, int, int, int);
float min_perimeter(int, int);

int main(void) {
	int trayh, trayw, slabh, slabw, min_area;
	float min_peri;

	printf("Enter size of tray: ");
	fflush(stdout);
	scanf("%d%d", &trayh, &trayw);

	printf("Enter size of slab: ");
	fflush(stdout);
	scanf("%d%d", &slabh, &slabw);

	min_area = min_unused_area(trayh, trayw, slabh, slabw);
	min_peri = min_perimeter(trayh, trayw);

	printf("Minimum unused area = %d\n", min_area);
	printf("Minimum perimeter after folding = %.2f", min_peri);
	return 0;
}

int min_unused_area(int trayh, int trayw, int slabh, int slabw) {
	int slabs1, slabs2;

	slabs1 = (trayh / slabh) * (trayw / slabw);
	slabs2 = (trayh / slabw) * (trayw / slabh);

	if (slabs1 > slabs2) {
		return (trayh * trayw) - (slabs1 * slabh * slabw);
	} else {
		return (trayh * trayw) - (slabs2 * slabh * slabw);
	}
}

float min_perimeter(int trayh, int trayw) {
	float h = trayh, w = trayw;

	for (int i = 0; i < 3; i++) {
		if (h > w) {
			h /= 2.0;
		} else {
			w /= 2.0;
		}
	}
	return (h + w) * 2;
}
