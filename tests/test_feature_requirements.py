#!/usr/bin/env python

import os
import sys
orch_dir = '/'.join(os.path.realpath(__file__).split('/')[:-2])
print ('Using orch modules from: %s' % orch_dir)
sys.path.insert(0, orch_dir)

from orch.features import requirements
from orch.deconf import format_flat_dict

def test_pool():
    p = {x.name:str(x.default) for x in requirements.pool.values()}
    r = format_flat_dict(p)
    assert r


if '__main__' == __name__:
    test_pool()
