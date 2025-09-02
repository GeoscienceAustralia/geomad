"""
Geomad: Geomedian and Median Absolute Deviation
"""

import sys
from setuptools import setup, Extension

try:
    import numpy as np
    include_dirs = [np.get_include()]
except ImportError:
    include_dirs = []

if sys.platform == 'darwin':
    # Needs openmp lib installed: brew install libomp
    cc_flags = ["-I/usr/local/include", "-Xpreprocessor", "-fopenmp"]
    ld_flags = ["-L/usr/local/lib", "-lomp"]
else:
    cc_flags = ['-fopenmp']
    ld_flags = ['-fopenmp']

extensions = [
    Extension(
        'geomad.pcm',
        ['geomad/pcm.pyx'],
        include_dirs=include_dirs,
        extra_compile_args=cc_flags,
        extra_link_args=ld_flags,
    ),
]

setup(
    ext_modules=extensions
)
