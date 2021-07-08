// copycat.c

#include <stdio.h>

void printfile(const char *filename) {
    int c;
    FILE *file = fopen(filename, "r");
    if (file) {
        while ((c = fgetc(file)) != EOF)
            putchar(c);
        fclose(file);
    }
}

int main(const int argc, const char **argv) {
    int c;
    if (argc > 1)
        for (int i = 1; i < argc; i++)
            printfile(argv[i]);
    else
        while ((c = getchar()) != EOF)
            putchar(c);
    return 0;
}
