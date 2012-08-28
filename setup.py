from distutils.core import setup, Command
import os, sys
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules=[
    Extension("pycaffeine",
        sources=["pycaffeine.pyx"],
        libraries=["lib/caffeine/caffeine"])
]

class CleanCommand(Command):
    description = "custom clean command that forcefully removes cython compilation files"
    user_options = []
    def initialize_options(self):
        self.cwd = None
    def finalize_options(self):
        self.cwd = os.getcwd()
    def run(self):
        assert os.getcwd() == self.cwd, 'Must be in package root: %s' % self.cwd
        os.system('rm -rf ./build ./pycaffeine.c ./pycaffeine.so')

setup(
    name = "PyCaffeine",
    cmdclass = {"build_ext": build_ext, "clean": CleanCommand},
    ext_modules = ext_modules
)


