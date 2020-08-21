import sys, os
from ctypes import CDLL, c_double

so_file = os.path.join( os.path.dirname( sys.argv[0] ), 'src', 'c_src', 'lib.so' )
c_lib = CDLL(so_file)
rootloop = c_lib.rootloop
rootloop.restype = c_double
