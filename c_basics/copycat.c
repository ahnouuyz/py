#include <stdio.h>

#define BUFFERSIZE 100

int main(int argc, const char *argv[]) {
	char buffer[BUFFERSIZE];
	FILE *fp = fopen(argv[1], "r");

	while (fgets(buffer, sizeof(buffer), fp) != NULL) {
		fprintf(stderr, "%s", buffer);
	}

	(void)fclose(fp);

	return 0;
}
