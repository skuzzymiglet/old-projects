#include <stdio.h>
#include "tinyexpr.h"

int main(){
    const char *expr = "6+8*99";
    printf("%f\n", te_interp(expr, 0));
    return 0;
}
