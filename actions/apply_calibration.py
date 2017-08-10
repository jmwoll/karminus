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
    apply_calibration(jobname=sys.argv[1],method=sys.argv[2],basis_set=sys.argv[3])
