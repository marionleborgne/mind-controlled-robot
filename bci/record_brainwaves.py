# -*- coding: utf-8 -*-

__author__ = 'marion'

"""
Record data from the Neurosky Mindwave mobile.
"""

import sys
import os
from consider import Consider

CWD = os.path.abspath(os.getcwd())

def record(out):
    con = Consider()
    for p in con.packet_generator():
        data = map(str, [p.low_alpha, p.high_alpha, p.low_beta, p.high_beta, p.attention, p.meditation, p.poor_signal])
        out.write(','.join(data))
        out.write('\n')


def main():
    #out = open("%s/test/data/mindwave.csv" % CWD, 'wb')
    out = sys.stdout


    try:
        record(out)
    except KeyboardInterrupt:
        if hasattr(out, 'close'):
            out.close()


if __name__ == '__main__':
    main()

