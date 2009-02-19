#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2009 José de Paula Eufrásio Júnior <jose.junior@gmail.com>

#    This file is part of Crisk.
#
#    Crisk is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Crisk is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
""" 
This is the basic package for the Crisk Application.
""" 

import sys
import os
from kiwi.environ import Library

# Adicionando paths para achar os resources

lib = Library('kiwi')
standalone_path = os.path.dirname(__file__)
if not hasattr(sys, 'frozen'):
    lib.add_global_resource('glade', 'glade')
    lib.add_global_resource('pixmaps', 'pixmaps')
    #environ.environ.add_resource('glade', standalone_path)

__version__ = '0.2'
__license__ = """
Copyright 2009 José de Paula Eufrásio Júnior <jose.junior@gmail.com>

This file is part of Crisk.

Crisk is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Crisk is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
"""