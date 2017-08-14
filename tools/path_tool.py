# Copyright (C) 2017  Jan Wollschläger <jmw.tau@gmail.com>
# This file is part of karminus.
#
# karminus is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os

def _script_dir():
	return os.path.dirname(os.path.realpath(__file__))

def project_dir():
	return os.path.dirname(_script_dir())

def xyz_dir():
	rslt = os.path.join(project_dir(),'xyz')
	#return os.path.join(rslt, 'default_db') + os.sep
	return os.path.join(rslt, 'through_space_db') + os.sep

def output_dir(basis_set=None, method=None):
	assert(basis_set is not None and method is not None)
	return os.path.join(os.path.join(project_dir(),'output'),
	 	method.lower() + "_" + basis_set.lower().replace('-','')) + os.sep
