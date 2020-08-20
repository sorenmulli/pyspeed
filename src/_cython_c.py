import sys, os
sys.path.append(os.path.join( os.path.dirname( sys.argv[0] ), 'src', 'cython_c_src' ))

from _cython_c_lib import rootloop #Remember to build cython
