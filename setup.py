from setuptools import find_packages
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(name='ur_ikfast',
      version='0.1.0',
      license='MIT License',
      long_description=open('README.md').read(),
      packages=find_packages(),
      ext_modules=[Extension("ur3e_ikfast",
                             ["ur3e/ur3e_ikfast.pyx",
                              "ur3e/ikfast_wrapper.cpp"], language="c++", libraries=['lapack']),
                  Extension("iscoin_ikfast",
                             ["iscoin/iscoin_ikfast.pyx",
                              "iscoin/ikfast_wrapper.cpp"], language="c++", libraries=['lapack'])
      ],
      cmdclass={'build_ext': build_ext})
