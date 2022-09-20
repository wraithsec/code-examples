#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    long count = strtol(argv[1], NULL, 10);
    if ( argc == 2) {
        printf("Computing and printing %i loops\n", count);
        for(int i = 0; i < count; i++) {
            printf("X");
            for(int in = count; in > 0; in--) {
                printf("Y");
            }
            printf("\n");
        }
        printf("\n");
    }
    else if ( argc > 2 ) { 
        printf("Too many arguments!\n");
        return 1; 
    }
}
