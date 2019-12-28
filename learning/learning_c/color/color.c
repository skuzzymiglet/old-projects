#include <stdio.h>

void color(char[15]);

void color(char name[15]){
    printf("\033");
    if(name == "red"){
        printf("[0;31m");
    }
    if(name == "blue"){
        printf("[0;34m");
    } 
    if(name == "green"){
        printf("[0;32m");
    }
    if(name == "yellow"){
        printf("[0;33m");
    }
    if(name == "reset"){
        printf("[0m");
    }
}
int main(){
    color("red");
    //printf("\033[1;34m");
    printf("Hello");
    color("blue");
    printf(" world!\n");
    color("green");
    printf("hoya!!\n");
    color("reset");
    //printf("\033[0m");
    return 0;
}
