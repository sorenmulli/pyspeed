#include <stdlib.h>
#include <math.h>

double rootloop(long N) {
    double x = 0;
    for (size_t i = 0; i < N; i += 2) {
        x += sqrt(i);
    }
    return x;
}
