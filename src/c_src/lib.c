# include <math.h>
# include <stdio.h>
double rootloop(long N) {
    double x = 0;
    long i;
    for (i = 0; i < N; i += 2) {
        x += sqrt(i);
    }
    return x;
}
