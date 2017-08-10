
The project karminus provides a common structure for ab initio nmr calculations.
While ab initio nmr calculations have come a long way, and are now
an established method in several branches of chemistry, e.g. for the
confirmation of absolute stereochemistry in natural products, there is
still no common framework for conveniently performing such computations.
Using karminus, chemical shift calculations are heavily automated by use of
python as the script language and ORCA 4.0.0 as the quantum chemistry program.

Therefore, running nmr chemical shift calculations is as easy as:
*) adding all calibration files to xyz/sub-directory/
*) running actions/calibrate_chemical_shifts.py on sub-directory
*) running actions/report_calibration.py to get calibration function
*) finally, running actions/apply_calibration.py to apply calibration on new
   instances
