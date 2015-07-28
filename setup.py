#!usr/bin/env python
from distutils.core import setup

setup(name='kicad_util',
      version='1.0', 
#      packages = ['sch','schlib','pcb'],
      py_modules = ['sch/sch','schlib/schlib','pcb/kicad_mod'],
     )
