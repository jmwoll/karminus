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


import math
import numpy as np
from matplotlib import pyplot as plt

def gauss(x,a,b,c):
    return a * math.e ** -((b-x)**2 /(2 * c**2))

def plot(spectrum,num_points=500,min_shift=-2,max_shift=14):
    ## iterate over all chemical shifts
    ## in the given spectrum.
    ## (label, shift, integral, multiplicity, coupling_constant)
    xs = np.linspace(min_shift,max_shift,num_points)
    ys = np.zeros(num_points)

    for entry in spectrum:
        if not "broadness" in entry:
            entry["broadness"] = 1
        if entry["mult"] == 1:
            ys += gauss(xs,entry["int"],entry["shift"],entry["broadness"])
    plt.plot(xs,ys,'-')
    plt.show()
