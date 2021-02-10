#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line_split = line.strip().split('\t')
    case = line_split[0]
    serviceTime = line_split[-1]
    print('%s\t%s' % (case, serviceTime))


