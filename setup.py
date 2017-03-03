import numpy

from distutils.core import setup
from Cython.Build import cythonize

setup(
    name='maze',
    ext_modules=cythonize('maze.pyx'),
    include_dirs=[numpy.get_include()],

)
