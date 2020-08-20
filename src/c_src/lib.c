# include <math.h>
int rootloop(int N) {
    int x = 0;
    int i;
    for (i = 0; i <= N; i+=2) {
        x += sqrt(i);
    }
    return x;
}
// Compile (in this folder) with
// gcc -shared -o lib.so lib.c
