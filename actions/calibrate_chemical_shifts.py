# Copyright (C) 2017-2018  Jan Wollschläger <janmwoll@gmail.com>
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
import sys
from karminus.tools import path_tool
from ORCAunleashed import orca

def calibrate_chemical_shifts(basis_set="aug-cc-pVDZ",
	method="B3LYP",xyz_dir=None):
	print("calibrating chemical shifts")
	print("this might take a while ...")
	if basis_set is None or str(basis_set).lower() == "none":
		basis_set = ""
	orca_input = """
!{} {} NMR

*xyzfile 0 1 guess.xyz
	""".format(basis_set,method).strip()

	print("calibration will be performed with the following orca input:")
	print(orca_input)

	project_dir = path_tool.project_dir()
	if xyz_dir is None:
		xyz_dir = path_tool.xyz_dir()
	else:
		if not path_tool.isdir(xyz_dir):
			xyz_dir = path_tool.xyz_parent_dir() + os.sep + xyz_dir + os.sep
	output_dir = path_tool.output_dir(basis_set=basis_set,method=method)

	print("all .xyz-files in {} will be used".format(xyz_dir))

	for xyzfile in os.listdir(xyz_dir):
		orca.run_orca(orca_input=orca_input,xyzfile=xyz_dir+xyzfile,
			jobname=xyzfile.split('.')[0],output_root_dir=output_dir)
		print("finished job", xyzfile.split('.')[0])


if __name__ == '__main__':
	import argparse
	from argparse import RawDescriptionHelpFormatter

	parser = argparse.ArgumentParser(description=(
	    """Creates a chemical shift calibration for all geometries in xyz\\default_db, e.g.

	    $ python calibrate_chemical_shifts.py --method BP86 --basis_set ccpVDZ

will carry out all chemical shift calculations necessary for the calibration.
	"""
	), formatter_class=RawDescriptionHelpFormatter)

	parser.add_argument('--method', nargs=1, help='the computational method, e.g. B3LYP')
	parser.add_argument('--basis_set', nargs=1, help='the basis set to use, e.g. ccpVDZ')
	parser.add_argument('--xyz_dir', nargs=1, help='the directory containing the xyz files used for calibration')
	args = parser.parse_args()
	calibrate_chemical_shifts(basis_set=args.basis_set[0], method=args.method[0], xyz_dir=args.xyz_dir[0])
