__author__ = 'Joel Akeret'
__email__ = 'jakeret@phys.ethz.ch'
__version__ = '0.1.0'
__credits__ = 'ETH Zurich, Institute for Astronomy'

DATETIME_FORMAT = "%Y-%m-%d-%H:%M:%S"
DATE_FORMAT = "%Y-%m-%d"

# Coords = namedtuple('Coords', ['ra', 'dec'])

class Coords:
    def __init__(self, ra, dec, az, el, t):
        self.ra = ra
        self.dec = dec
        self.az = az
        self.el = el
        self.t = t
