#include <stdio.h>

#define BUFFERSIZE 100

int main(void) {
	char buffer[BUFFERSIZE];

	while (fgets(buffer, sizeof(buffer), stdin) != NULL) {
		fprintf(stderr, "%s", buffer);
	}

	return 0;
}
