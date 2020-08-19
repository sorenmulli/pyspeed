cpdef int rootloop(int N):
    cdef int x = 0
    cdef int i
    for i in range(0, N, 2):
        x += i ** (1/2)
    return x
