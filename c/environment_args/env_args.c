#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <stdbool.h>
#define BUFSIZE 80

int main(int argc, char* argv[]){
    char varabc[BUFSIZE];
    char *envvar = "ABC";
    size_t i = 0;
    char *token; 


    
    // Get cmdline Args
    printf("Num of args %d\n", argc);
    for (i = 1; i < argc; i++)
    {
        printf("argv[%u] = %s\n", i, argv[i]);
    }


    // Doing getopt on the cmdline args 
    int opt;
    while ((opt = getopt(argc, argv, "ab:")) != -1){
        switch (opt) { 
        case 'a': printf("A ..\n"); break;
        case 'b': printf("B = %s\n", optarg); break;
        default:
            printf("Usage: %s [-ab] [file]\n", argv[0]);
            exit(EXIT_FAILURE);
        }
    }


    // Make sure envvar isnt empty.
    if(!getenv(envvar)){
        fprintf(stderr, "Env var %s was not found.\n", envvar);
        exit(1);
    }

    // Make envvar it isnt too small.
    if(snprintf(varabc, BUFSIZE, "%s", getenv(envvar)) >= BUFSIZE){
        fprintf(stderr, "BUFSIZE of %d was too small. Aborting\n", BUFSIZE);
        exit(1);
    }

    // Token the varabc and split it up.
    token = strtok(varabc, " ");
    size_t cnt = 0;
    cnt++;
    while( token != NULL ){
        printf("env[%d]: %s\n", cnt, token);
        cnt++;
        token = strtok(NULL, " ");
    } 
    
        

    return 0;
}
