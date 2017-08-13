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

from karminus.actions import report_calibration
from karminus.tools import path_tool
from ORCAunleashed import orca,tools
import sys

def apply_calibration(jobname=None,basis_set=None, method=None, nuclei_type=None):
    if nuclei_type is None:
        nuclei_type = 'H'
    rep = orca.reporter_by_name(jobname,output_root_dir=path_tool.output_dir(basis_set=basis_set, method=method))
    calib = report_calibration.report_calibration(basis_set=basis_set,method=method,nuclei_type=nuclei_type)
    c_shifts = { }
    uncal_c_shifts = tools.chemical_shifts(rep)
    for key in uncal_c_shifts:
        if nuclei_type not in key:
            continue
        c_shifts[key] = uncal_c_shifts[key]*calib['slope']+calib['intercept']
    print(c_shifts)
    return c_shifts


if __name__ == '__main__':
    import argparse
    from argparse import RawDescriptionHelpFormatter

    parser = argparse.ArgumentParser(description=(
        """Given the computational method <method> and the basis_set <basis_set>,
    actions\\apply_calibration.py applies the calibration created before
    with actions\\calibrate_chemical_shifts.py to the given <jobname>. For example,

        $ python apply_calibration.py --jobname aniline --method BP86 --basis_set ccpVDZ --nuclei_type H

    will apply the calibration to aniline and output the chemical shifts.
    """
    ), formatter_class=RawDescriptionHelpFormatter)


    parser.add_argument('--jobname', nargs=1, help='name of job, i.e. for "benzene.xyz" jobanem would be "benzene"')
    parser.add_argument('--method', nargs=1, help='the computational method, e.g. B3LYP')
    parser.add_argument('--basis_set', nargs=1, help='the basis set to use, e.g. ccpVDZ')
    parser.add_argument('--nuclei_type', nargs=1, help='the type of nuclei for which to compute chemical shifts, defaults to "H"')

    args = parser.parse_args()

    if not args.nuclei_type:
        args.nuclei_type = ["H"]
    apply_calibration(jobname=args.jobname[0],method=args.method[0],basis_set=args.basis_set[0],nuclei_type=args.nuclei_type[0])
