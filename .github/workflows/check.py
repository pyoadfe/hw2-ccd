#!/usr/bin/env python3

import json
import sys
from numpy.testing import assert_almost_equal

with open(sys.argv[1]) as json_file:
    data = json.load(json_file)

    assert_almost_equal(data['ron'], 15, 0)
    assert_almost_equal(data['ron_err'], 1.3, 0.75)
    assert_almost_equal(data['gain'], 2.1, 1)
    assert_almost_equal(data['gain_err'], 0.03, 2)
