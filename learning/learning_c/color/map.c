#include <stdio.h>
#define WIDTH 10
#define HEIGHT 5


char colors[HEIGHT][WIDTH] ={
    "==========",
    "#rbgyygbr#",
    "#rbgyybgr#",
    "#rbgyygbr#",
    "=========="};

char letters[HEIGHT][WIDTH] = {
    "/^^^^^^^^\\",
    "|oooooooo|",
    "|oooooooo|",
    "|oooooooo|",
    "\\________/"
    };

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
    printf("hoya!!\n\n\n\n");
    color("reset");
    for(int x = 0; x <= HEIGHT-1; x++){
         for(int y = 0; y <= WIDTH-1; y++){
             if(colors[x][y] == 'r'){
                 color("red");
             }
             if(colors[x][y] == 'g'){
                 color("green");
             }
             if(colors[x][y] == 'b'){
                 color("blue");
             }
             if(colors[x][y] == 'y'){
                 color("yellow");
             }
             putchar(letters[x][y]);
             color("reset");
         }
         printf("\n");
    }
    //printf("\033[0m");
    return 0;
}
