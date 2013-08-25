import numpy

from setuptools import setup
from distutils.extension import Extension

# setuptools DWIM monkey-patch madness
# http://mail.python.org/pipermail/distutils-sig/2007-September/thread.html#8204
import sys
if 'setuptools.extension' in sys.modules:
    m = sys.modules['setuptools.extension']
    m.Extension.__dict__ = m._Extension.__dict__

define_macros = [('VOID', 'int'),
                 ('REAL', 'double'),
                 ('NO_TIMER', 1),
                 ('TRILIBRARY', 1),
                 ('ANSI_DECLARATORS', 1)]

cytriangle = Extension(
    'triangle.core',
    sources = ['c/triangle.c', 'triangle/c_triangle.pxd', 'triangle/core.pyx'],
    include_dirs = ['c'],
    define_macros = define_macros)

setup(name='triangle',
      packages=['triangle'],
      package_dir={'triangle':'triangle'},
      version='2013.01.07',
      description='Python binding to the triangle library',
      author='Dzhelil Rufat',
      author_email='drufat@caltech.edu',
      license='GNU LGPL',
      url='http://drufat.github.com/triangle',
      requires = ['numpy (>=1.7.0)',
                  'cython (>=0.18)'],
      setup_requires=[
          'setuptools_cython',
      ],
      ext_modules=[ cytriangle ]
)
