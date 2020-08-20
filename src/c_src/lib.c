# include <math.h>
long rootloop(int N) {
    long x = 0;
    long i;
    for (i = 0; i <= N; i += 2) {
        x += sqrt(i);
    }
    return x;
}
// Compile (in this folder) with
// gcc -shared -o lib.so lib.c
