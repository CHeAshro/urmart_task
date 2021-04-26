
import sys


if 'test' in sys.argv:
    from urmart.settings.test import *
else:
    from urmart.settings.settings import *
