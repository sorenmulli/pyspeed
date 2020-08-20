# include <math.h>
double rootloop(int N) {
    double x = 0;
    double i;
    for (i = 0; i <= N; i += 2) {
        x += sqrt(i);
    }
    return x;
}
// Compile (in this folder) with
// gcc -shared -o lib.so lib.c
