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


# dict containing the experimentally observed chemical shifts
e_shifts = {}

# Important:
# Atoms are numbered by the sequence as they appear in the xyz-file.
# Programs like Avogadro or Gabedit should use the same enumeration.
# If several H-atoms are homotopic (e.g. Hs in a methyl group), all
# homotopic Hs in the xyz-file are specified separated by a comma, e.g.
# if Hatoms 4,5,6 are part of the same methyl group and the chemical
# shift would be 1.3 ppm, it would be specified as
# "4,5,6H": 1.3
# the averaging of the corresponding computed chemical shifts will
# be handled internally by actions/report_calibration.py
#

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# 2_methyl_oxirane
e_shifts["2_methyl_oxirane"] = {
	"2H": 2.745,
	"1H": 2.427,
	"3H": 2.979,
	"4,5,6H": 1.316,
	"1C": 48.17,
	"2C": 47.94,
	"3C": 18.08
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# acrylaldehyde
e_shifts["acrylaldehyde"] = {
	"4H": 9.586,
	"3H": 6.37,
	"2H": 6.522,
	"1H": 6.35,
	"1C": 137.96,
	"2C": 138.53,
	"3C": 194.44,
 }

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# acetaldehyde
e_shifts["acetaldehyde"] = {
	"1,2,3H": 2.206,
	"4H": 9.789,
	"1C": 30.89,
	"2C": 199.93,
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# acetaldehyde_dimethyl_acetale
e_shifts["acetaldehyde_dimethyl_acetale"] = {
	"5,6,7,8,9,10H": 3.309,
	"1,2,3H": 1.281,
	"4H": 4.568,
	"1C": 18.80,
	"2C": 101.24,
	"3,4C": 52.31,
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# acrylonitrile
e_shifts["acrylonitrile"] = {
	"3H": 5.69,
	"2H": 6.24,
	"1H": 6.11,
	"3C": 117.13,
	"2C": 107.81,
	"1C": 137.52,
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ethyl_acrylate
e_shifts["ethyl_acrylate"] = {
	"1H": 6.369,
	"2H": 5.811,
	"3H": 6.130,
	"4,5H": 4.214,
	"6,7,8H": 1.302,
	"1C": 130.31,
	"2C": 128.88,
	"3C": 166.18,
	"4C": 60.48,
	"5C": 14.28,
}



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ethyl_pivalate
e_shifts["ethyl_pivalate"] = {
	"1,2,3,4,5,6,7,8,9H": 1.195,
	"10,11H": 4.112,
	"12,13,14H": 1.247,
	"3,4,5C": 27.28,
	"1C": 38.71,
	"6C": 51.68,
	"7C": 14.25,
	"2C": 178.28,
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# propionaldehyde
e_shifts["propionaldehyde"] = {
	"1,2,3H": 1.113,
	"4,5H":  2.46,
	"6H": 9.793,
	"1C": 6.04,
	"2C": 37.28,
	"3C": 203.21,
}



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# propionitrile
e_shifts["propionitrile"] = {
	"1C": 120.97,
	"2C": 10.93,
	"3C": 10.60,
	"1,2H": 2.36,
	"3,4,5H": 1.30,
}


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# tetrahydrofuran_2_4_dione
e_shifts["tetrahydrofuran_2_4_dione"] = {
	"1C": 87.62,
	"2C": 174.38,
	"3C": 180.52,
	"4C": 67.86,
	"1H": 4.952,
	"2H": 12.6,
	"3,4H": 4.655,
}



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# acetic_acid
e_shifts["acetic_acid"] = {
	"1C": 20.80,
	"2C": 178.12,
	"1,2,3H": 2.098,
	#"4H": 11.42,  # COOH
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# acetone
e_shifts["acetone"] = {
	"1,3C": 30.81,
	"2C": 206.55,
	"1,2,3,4,5,6H": 2.162,
}




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# phenol
e_shifts["phenol"] = {
	"1,5C": 115.48,
	"2,4C": 129.79,
	"3C": 121.09,
	"6C": 155.02,
	"2,4H": 6.838,
	"3,5H": 7.240,
	"6H": 6.931,
	#"1H": 5.35, # OH
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# meta_cresol
e_shifts["meta_cresol"] = {
	"1C": 112.51,
	"2C": 129.51,
	"3C": 121.86,
	"4C": 139.92,
	"5C": 116.26,
	"6C": 155.07,
	"7C": 21.24,
	"5,8H": 6.64,
	"6H": 7.117,
	"7H": 6.750,
	"1,2,3H": 2.297,
	#"4H": 5.06, # OH
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ortho_cresol
e_shifts["ortho_cresol"] = {
	"1C": 115.12,
	"2C": 127.12,
	"3C": 120.94,
	"4C": 131.14,
	"5C": 124.15,
	"6C": 153.58,
	"7C": 15.72,
	"2H": 6.74,
	"3H": 7.07,
	"4H": 6.82,
	"5H": 7.11,
	"6,7,8H": 2.236,
	#"1H": 4.79,# OH
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# para_cresol
e_shifts["para_cresol"] = {
	"1,5C": 115.39,
	"2,4C": 130.17,
	"3C": 130.17,
	"6C": 152.92,
	"7C": 20.39,
	"2,4H": 6.721,
	"3,5H": 7.002,
	"6,7,8H": 2.254,
	#"1H": 5.20, # OH
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# meta_amino_phenol
e_shifts["meta_amino_phenol"] = {
	"1C": 103.42,
	"2C": 129.30,
	"3C": 105.46,
	"4C": 149.63,
	"5C": 101.48,
	"6C": 158.00,
	"2H": 6.01,
	"3H": 6.018,
	"4H": 6.780,
	"5H": 5.942,
	#"1H": 8.83, # OH
	#"6,7H": , # NH2
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# ortho_amino_phenol
e_shifts["ortho_amino_phenol"] = {
	"1C": 114.47,
	"2C": 116.48,
	"3C": 119.47,
	"4C": 114.44,
	"5C": 136.40,
	"6C": 143.95,
	"2H": 6.649,
	"3H": 6.587,
	"4H": 6.400,
	"5H": 6.543,
	#"1H": 8.9, # OH
	#"6,7H": 4.4, # NH2
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# nitrobenzene
e_shifts["nitrobenzene"] = {
	"1,5C": 123.46,
	"2,4C": 129.43,
	"3C": 134.71,
	"6C": 148.30,
	"1,2H": 8.245,
	"3,5H": 7.557,
	"4H": 7.705,
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# chlorobenzene
e_shifts["chlorobenzene"] = {
	"1,5C": 128.63,
	"2,4C": 129.72,
	"3C": 126.43,
	"6C": 134.33,
	#"1,2H": , higher order spectrum -> "one big multiplet"
	#"3,5H": ,
	#"4H": ,
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# aniline
e_shifts["aniline"] = {
	"1,5C": 115.07,
	"2,4C": 129.26,
	"3C": 118.39,
	"6C": 146.51,
	"1,2H": 6.64,
	"3,5H": 7.12,
	"4H": 6.73,
	#"6,7H": 3.55, # NH2
}
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #
# phenylacetylene
e_shifts["phenylacetylene"] = {
	"1,5C": 132.11,
	"2,4C": 128.29,
	"3C": 128.74,
	"6C": 122.17,
	"7C": 83.67,
	"8C": 77.26,
	"1,2H": 7.48,
	"3,5H": (7.40+7.21)/2.0,
	"4H": (7.40+7.21)/2.0,
	"6H": 3.057,
}

# benzonitrile
e_shifts["benzonitrile"] = {
	"1,5C": 132.10,
	"2,4C": 129.21,
	"3C": 132.84,
	"6C": 112.41,
	"7C": 118.82,
	#"1,2H": 7.33 # => higher order spectrum one big multiplet
}
