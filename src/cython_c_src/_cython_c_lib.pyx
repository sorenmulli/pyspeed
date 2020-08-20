# cython: language_level=3
cpdef double rootloop(int N):
    cdef double x = 0
    cdef int i
    for i in range(0, N, 2):
        x += i ** (.5)
    return x
