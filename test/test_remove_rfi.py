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
Created on Jan 7, 2015

@author: seehars
"""

import numpy as np

from ivy.utils.struct import Struct
from seek.plugins import remove_rfi


class TestRemoveRfiPlugin:

    def setup(self):
        params = Struct(cleaner="seek.mitigation.outlier_masking",
                        multiplicator=5)
        self.ctx = Struct(params=params,
                          tod_vx=np.ma.array([[1]]),
                          tod_vy=np.ma.array([[1]]))

    def test_remove_rfi(self):
        remove_rfi_plugin = remove_rfi.Plugin(self.ctx)
        remove_rfi_plugin.run()
        assert not self.ctx.tod_vx.mask
        assert not self.ctx.tod_vy.mask
