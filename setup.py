from setuptools import setup
from setuptools import Extension
import numpy


conv_ext = Extension(
    'conv_func',
    ['conv_func.c']
)

pool_max_ext = Extension(
    'pooling_max_func',
    ['pooling_max_func.c']
)

pool_avg_ext = Extension(
    'pooling_avg_func',
    ['pooling_avg_func.c']
)

setup(
    name='nn-func-lib',
    version='3.3',
    install_requires=['numpy'],
    ext_modules=[
        conv_ext,
        pool_max_ext,
        pool_avg_ext
    ],
    include_dirs=[numpy.get_include()]
)
