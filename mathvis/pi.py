#! /usr/bin/env python
# vim: set fileencoding=utf-8: set encoding=utf-8:

def join_digits(digits, base=10):
    value = 0
    for d in digits:
        value = (value*10) + d
    return value

def adjacent_pairs(digits, width=1):
    """
    Given a sequence of digits, yields two-tuples of numeric values of adjacent
    pairs of digits from the sequence. For instance, the sequence:

        1, 2, 3, 4, 5, 6, 7

    would generate the following pairs:

        1, 2
        2, 3
        3, 4
        4, 5
        5, 6
        6, 7

    Or, if you specify a width of 2 (instead of the default 1):

        12, 23
        23, 34
        34, 45
        45, 56
        56, 67

    """
    subseq = []
    for d in digits:
        if len(subseq) == width:
            a = tuple(subseq)
            del(subseq[0])
            subseq.append(d)
            b = tuple(subseq)
            yield (join_digits(a), join_digits(b))
        else:
            subseq.append(d)

def digits_of_pi(filename):
    with open(filename, 'r') as fid:
        while True:
            c = fid.read(1)
            if len(c) != 1:
                break
            if c.isdigit():
                yield int(c)

if __name__ == '__main__':
    import random

    w = 4
    pi_digits = adjacent_pairs(digits_of_pi(r'data\pi\100_000.txt'), w)
    rand_digits = adjacent_pairs((random.randint(0, 9) for i in xrange(100000)), w)
    try:
        for i in xrange(10000):
            pa, pb = pi_digits.next()
            ra, rb = rand_digits.next()
            print pa, pb, ra, rb
    except StopIteration:
        pass


