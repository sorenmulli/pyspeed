import os, sys
import ctypes

rust_lib = ctypes.CDLL(
    os.path.join(
        os.path.dirname(sys.argv[0]),
        'src', 'rust_src', 'target', 'release', 'librust_src.so'
    )
)
rootloop = rust_lib.rootloop

