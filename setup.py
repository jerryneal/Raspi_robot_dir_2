'''
	Description : This is a setup file for the py2LinkArm program.
'''

from distutils.core import setup
from distutils.extension import Extension
from Cython.distutils import build_ext

setup (
		cmdclass = {'build_ext' : build_ext},
		ext_modues = [Extension("py2LinkArm",
			soruces = ["py2LinkArm.pyx"],
			language = "c++"),],
		)