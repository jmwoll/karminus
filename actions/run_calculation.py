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
    run_calculation(xyzfile=sys.argv[1],method=sys.argv[2],basis_set=sys.argv[3])
