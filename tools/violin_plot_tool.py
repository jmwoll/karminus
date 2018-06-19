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

from karminus.actions import report_calibration

def violin_plot(rep): #method=None,basis_set=None,nuclei_type=None):
    #rep = report_calibration.report_calibration(**locals())#method=method,basis_set=basis_set,nuclei_type=nuclei_type)
    from matplotlib import pyplot as plt
    import seaborn as sns

    pxs,pys = rep['pxs'],rep['pys']
    plt.figure(figsize=(3,6))
    ax = sns.violinplot(y=pys)
    plt.show()

if __name__ == '__main__':
    import argparse
    from argparse import RawDescriptionHelpFormatter

    parser = argparse.ArgumentParser(description=(
        """Prints a violin plot for the calibration. For example,

        $ python violin_plot.py --method BP86 --basis_set ccpVDZ --nuclei_type H

    will show a violin plot of the EXPERIMENTAL 1H chemical shifts calibration.
    (The method and basis_set are just needed to execute actions/report_calibration
    internally.)
    """
    ), formatter_class=RawDescriptionHelpFormatter)

    parser.add_argument('--method', nargs=1, help='the computational method, e.g. B3LYP')
    parser.add_argument('--basis_set', nargs=1, help='the basis set to use, e.g. ccpVDZ')
    parser.add_argument('--nuclei_type', nargs=1, help='the type of nuclei for which to compute chemical shifts, defaults to "H"')
    args = parser.parse_args()

    violin_plot(method=args.method[0],basis_set=args.basis_set[0],nuclei_type=args.nuclei_type[0])
