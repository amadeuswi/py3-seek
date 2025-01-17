# SEEK is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# SEEK is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with SEEK.  If not, see <http://www.gnu.org/licenses/>.


"""
Created on Feb 26, 2016

author: jakeret
"""

import numpy as np


def get_mapped_values(re_data, ctx):
    """
    Maps the data by simply computing the variance per pixel
    :param re_data: data in the restructured form after create_maps.py

    :return: variance and sum of unmasked data
    """

    return re_data.var(axis=1), np.sum(~re_data.mask, axis=1)
