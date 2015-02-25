#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:

import math

def count_residues(numbers, base=10):
    counts = [0 for i in xrange(base)]
    for n in numbers:
        r = n % base
        counts[r] += 1
    return counts

def get_primes(filename=r'data\primes\100_000.txt'):
    with open(filename, 'r') as fid:
        for line in fid:
            if line:
                yield int(line)

if __name__ == '__main__':
    base = 70

    brange = range(base)
    theta = (2.0 * math.pi) / float(base-1)
    counts = count_residues(get_primes(), base)
    total = float(sum(counts))
    pcts =  [float(counts[i]) / total for i in brange]
    max_pct = max(pcts)
    for i in brange:
        print i, i*theta, counts[i], pcts[i], pcts[i] / max_pct


