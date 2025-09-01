"""
Geomad: Geomedian and Median Absolute Deviation
"""

import sys
from setuptools import setup, find_packages, Extension

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

build_cfg = dict(
    include_dirs=include_dirs,
    extra_compile_args=cc_flags,
    extra_link_args=ld_flags,
)
print(build_cfg)

extensions = [
    Extension('geomad.pcm', ['geomad/pcm.pyx'], **build_cfg),
]

tests_require = [
    "pytest",
    "joblib",
]

setup(
    name="geomad",
    packages=find_packages(".", exclude=['tests']),
    include_package_data=True,
    package_data={'': ['geomad/*.pyx', 'geomad/*.pyx', 'geomad/*.h', 'geomad/*.c']},
    setup_requires=["Cython>=0.29", "numpy<2"],
    install_requires=["numpy<2"],
    extras_require={
        'test': tests_require,
    },
    version="1.0.0rc1",
    description="Geomad.",
    url="http://github.com/GeoscienceAustralia/geomad",
    author="GeoscienceAustralia",
    author_email="",
    license="Apache 2.0",
    zip_safe=False,
    ext_modules=extensions
)
