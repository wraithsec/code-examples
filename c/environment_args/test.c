#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#define BUFSIZE 80

int main(int argc, char* argv[]){
    char *s[32];
    int i = 0;

    s[i++]="-i";
    s[i++]="127.0.0.1";
    s[i++]="/var/lib/shadow";

    for (i = 0; s[i] != NULL; i++) {
        printf(i);
    }

    return 0;
}
