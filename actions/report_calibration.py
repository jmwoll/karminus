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

import sys
import re
from ORCAunleashed import orca,tools
from karminus.experiment import exp_chemical_shifts
from karminus.tools import path_tool
from matplotlib import pyplot as plt
from scipy.stats import linregress

def report_calibration(basis_set=None, method=None, nuclei_type=None):
	calib_report = { }
	comp_shifts = { }

	e_shifts = exp_chemical_shifts.e_shifts

	if nuclei_type is None:
		nuclei_type = 'H'

	for exp in e_shifts:
		rep = orca.reporter_by_name(exp,output_root_dir=path_tool.output_dir(basis_set=basis_set, method=method))
		c_shifts = tools.chemical_shifts(rep)
		for e_atom in e_shifts[exp]:
			if ',' in e_atom:
				labs = e_atom.split(',')
				labs = [re.sub('[a-zA-Z]','',lab) for lab in labs]
				atom_type = re.sub('[0-9,]','',e_atom)
				homotopic_shifts = [c_shifts[lab+atom_type] for lab in labs]
				c_shifts[e_atom] = sum(homotopic_shifts)/float(len(homotopic_shifts))
		comp_shifts[exp] = c_shifts


	#nuclei_type = 'C'

	pxs,pys = [],[]
	for exp in e_shifts:
		for shift_lab in e_shifts[exp]:
			if not nuclei_type in shift_lab:
				continue
			# strong outlier due to tautomerism, remove for now...
			if 'H' in shift_lab and exp == 'tetrahydrofuran_2_4_dione':
				if shift_lab == '2H':
					continue
			pys.append(e_shifts[exp][shift_lab])
			pxs.append(comp_shifts[exp][shift_lab])

	plt.plot(pxs,pys,'bo')


	slope, intercept, r_value, p_value, std_err = linregress(pxs, pys)
	print("slope {} | intercept {} | r2 {} | stddev {}".format(
		slope,intercept,r_value**2,std_err))

	calib_report['slope'],calib_report['intercept'] = slope,intercept
	calib_report['r_value'],calib_report['p_value'] = r_value,p_value
	calib_report['std_err'] = std_err

	plt.plot(pxs, [slope*x + intercept for x in pxs], 'r--')
	plt.show()


	pxs = [x * slope + intercept for x in pxs]

	from sklearn.metrics import mean_squared_error, mean_absolute_error
	from math import sqrt

	rms = sqrt(mean_squared_error(pxs, pys))
	mae = mean_absolute_error(pxs, pys)
	print("RMS",rms)
	print("MAE", mae)

	calib_report['rms'],calib_report['mae'] = rms,mae

	print("The database has {} entries".format(
		len(e_shifts)
	))

	count = 0
	for exp in e_shifts:
		count += len([shift for shift in e_shifts[exp] if nuclei_type in shift])

	print("with {} chemical shifts".format(count))
	return calib_report

if __name__ == '__main__':
	report_calibration(method=sys.argv[1],basis_set=sys.argv[2])
