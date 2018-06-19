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

from ORCAunleashed import orca
from karminus.tools import path_tool
import sys,os

def run_calculation(xyzfile=None,basis_set=None,method=None):
    assert(xyzfile is not None)
    assert(basis_set is not None)
    assert(method is not None)
    orca_input = """
!{} {} NMR

*xyzfile 0 1 guess.xyz
""".format(basis_set,method).strip()
    project_dir = path_tool.project_dir()
    output_dir = path_tool.output_dir(basis_set=basis_set,method=method)
    orca.run_orca(orca_input=orca_input,xyzfile=xyzfile,
        jobname=(xyzfile.split(os.sep)[-1]).split('.')[0],output_root_dir=output_dir)


if __name__ == '__main__':
    import argparse
    from argparse import RawDescriptionHelpFormatter

    parser = argparse.ArgumentParser(description=(
        """Given the xyzfile <xyzfile>, computational method <method> and the basis_set <basis_set>,
    actions\\run_calculation.py runs an NMR calculation. For example,

        $ python run_calculation.py --xyzfile patho-to-xyzfile.xyz --method BP86 --basis_set ccpVDZ

    will run the appropriate BP86//ccpVDZ NMR job.
    """
    ), formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument('--xyzfile', nargs=1, help='the file-path of the xyzfile')
    parser.add_argument('--method', nargs=1, help='the computational method, e.g. B3LYP')
    parser.add_argument('--basis_set', nargs=1, help='the basis set to use, e.g. ccpVDZ')
    parser.add_argument('--nuclei_type', nargs=1, help='the type of nuclei for which to compute chemical shifts, defaults to "H"')
    args = parser.parse_args()

    run_calculation(xyzfile=args.xyzfile[0],method=args.method[0],basis_set=args.basis_set[0])
