import os, sys
import ctypes

rust_lib = ctypes.CDLL( os.path.dirname( sys.argv[0] ), 'rust_src', 'liblib.so' )
rootloop = rust_lib._FuncPtr
