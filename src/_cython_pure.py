import sys, os
sys.path.append(os.path.join( os.path.dirname( sys.argv[0] ), 'cython_pure_src' ))

from _cython_pure_lib import rootloop #Remember to build cython
