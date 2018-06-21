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

import sys
import re
from collections import defaultdict
from ORCAunleashed import orca,tools
from karminus.experiment import default_db_exp_chemical_shifts
from karminus.tools import load_tool,path_tool,log_tool
from karminus.tools import violin_plot_tool
from matplotlib import pyplot as plt
from scipy.stats import linregress

log = log_tool.logger(__name__)


def _average_conformers(e_shifts,conformer_indicator):
	def avg(lst):
		return sum(lst) / float(len(lst))
	rslt = defaultdict(lambda: {})
	for exp in e_shifts:
		for shift_lab in e_shifts[exp]:
			trunc_exp = exp
			if conformer_indicator in exp:
				trunc_exp = exp.split(conformer_indicator)[0]
			if trunc_exp in rslt and shift_lab in rslt[trunc_exp]:
				rslt[trunc_exp][shift_lab].append(e_shifts[exp][shift_lab])
			else:
				rslt[trunc_exp][shift_lab] = [e_shifts[exp][shift_lab]]
	log.debug(rslt)
	new_rslt = defaultdict(lambda: {})
	for exp in rslt:
		for shift_lab in rslt[exp]:
			new_rslt[exp][shift_lab] = avg(rslt[exp][shift_lab])
	return new_rslt
	#return { k: avg(v) for k,v in rslt }

def _extend_conformers(e_shifts,conf_ind,max_confs):
	rslt = { }
	for k in e_shifts:
		for idx in range(1,max_confs+1):
			rslt[k+conf_ind+"_{}".format(idx)] = e_shifts[k]
		rslt[k] = e_shifts[k]
	return rslt



def report_calibration(basis_set=None, method=None, nuclei_type=None, overall_runtime=None, json=None, violin_plot=None, average_conformers=True, conformer_indicator="__conf",
	max_conformers=10):
	if overall_runtime is None or overall_runtime.lower() == 'false':
		overall_runtime = False
	import seaborn as sns
	calib_report = { }
	comp_shifts = { }

	e_shifts = None
	if json is None:
		e_shifts = default_db_exp_chemical_shifts.e_shifts
	else:
		e_shifts = load_tool.chemical_shifts_from_json_file(json)

	assert(e_shifts is not None)

	extended_e_shifts = e_shifts
	if average_conformers:
		extended_e_shifts = _extend_conformers(e_shifts,conformer_indicator,max_conformers)

	if nuclei_type is None:
		nuclei_type = 'H'

	for exp in extended_e_shifts:
		print(exp)
		rep = orca.reporter_by_name(exp,output_root_dir=path_tool.output_dir(basis_set=basis_set, method=method))
		c_shifts = None
		try:
			c_shifts = tools.chemical_shifts(rep)
		except:
			print("skipping on experiment {}, because file was not found".format(exp))
		if c_shifts is None:
			continue
		for e_atom in extended_e_shifts[exp]:
			if ',' in e_atom:
				labs = e_atom.split(',')
				labs = [re.sub('[a-zA-Z]','',lab) for lab in labs]
				atom_type = re.sub('[0-9,]','',e_atom)
				homotopic_shifts = [c_shifts[lab+atom_type] for lab in labs]
				c_shifts[e_atom] = sum(homotopic_shifts)/float(len(homotopic_shifts))
		comp_shifts[exp] = c_shifts

	if average_conformers:
		comp_shifts = _average_conformers(comp_shifts, conformer_indicator)

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

	calib_report['pxs'] = pxs
	calib_report['pys'] = pys

	log.debug('eshifts {}'.format(e_shifts))
	log.debug('pxs {}'.format(pxs))
	log.debug('pys {}'.format(pys))

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
	if overall_runtime:
		overall_runtime = 0.0
		for exp in e_shifts:
			rep = orca.reporter_by_name(exp,output_root_dir=path_tool.output_dir(basis_set=basis_set, method=method))
			overall_runtime += tools.run_time(rep)

	print("overall runtime: {} minutes".format(overall_runtime))

	if violin_plot:
		log.debug('VIOLIN PLOT')
		violin_plot_tool.violin_plot(calib_report)

	return calib_report

if __name__ == '__main__':
	import argparse
	from argparse import RawDescriptionHelpFormatter

	parser = argparse.ArgumentParser(description=(
	    """Given the computational method <method> and the basis_set <basis_set>,
	actions\\report_calibration.py reports the current calibration that has been created before
	with actions\\calibrate_chemical_shifts.py. For example,

	    $ python report_calibration.py --method BP86 --basis_set ccpVDZ --nuclei_type C

	will show the calibration for 13C nuclei using basis_set cc-pVDZ and BP86 functional.
	The calibration function will be shown and it's slope, intercept is given.
	Furthermore, statistics like r^2 value, standard deviation, mean absolute error
	and mean square root error are reported.
	"""
	), formatter_class=RawDescriptionHelpFormatter)

	parser.add_argument('--method', nargs=1, help='the computational method, e.g. B3LYP')
	parser.add_argument('--basis_set', nargs=1, help='the basis set to use, e.g. ccpVDZ')
	parser.add_argument('--nuclei_type', nargs=1, help='the type of nuclei for which to compute chemical shifts, defaults to "H"')
	parser.add_argument('--overall_runtime', nargs=1, help='prints overall runtime')
	parser.add_argument('--json', nargs=1, help='the json file containing the experimental chemical shifts')
	parser.add_argument('--violin_plot', action="store_true", help="makes a violin plot of the chemical shifts")
	parser.add_argument('--confs', action="store_true", help="considers additional conformers if provided as additional xyz files")
	args = parser.parse_args()
	if not args.overall_runtime:
		args.overall_runtime = [None]
	report_calibration(method=args.method[0],basis_set=args.basis_set[0],
		nuclei_type=args.nuclei_type[0],overall_runtime=args.overall_runtime[0],violin_plot=args.violin_plot,json=args.json[0],average_conformers=args.confs)
