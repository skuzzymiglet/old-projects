#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#define WIDTH 2
#define HEIGHT 2

void waitFor(unsigned int secs);

void waitFor (unsigned int secs) {
    unsigned int retTime = time(0) + secs;   // Get finishing time.
    while (time(0) < retTime);               // Loop until it arrives.
}

/*char colors[HEIGHT][WIDTH] ={
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
    };*/ 

struct frame {
    char colors[HEIGHT][WIDTH];
    char letters[HEIGHT][WIDTH];
} frames[] = {
    {"r ","  "}, {"o ","  "},
    {" r","  "}, {" o","  "},
    {"  ","r "}, {"  ","o "},
    {"  "," r"}, {"  "," o"}
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
    //char colors[HEIGHT][WIDTH] = frames[0].colors;
    //char letters[HEIGHT][WIDTH] = frames[0].letters;
    /*for(int x = 0; x <= HEIGHT-1; x++){
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
         waitFor(0.5);
    system("@cls||clear");}*/ 
    printf( frames[0].colors[0]);
    return 0;
}
