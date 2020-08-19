from distutils.core import setup
from Cython.Build import cythonize

# Build: Do (in this folder)
# python setup.py build_ext --inplace
setup(ext_modules=cythonize('_cython_c_lib.pyx'))

# (when using anaconda, you might have to run conda install gxx_linux-64)
