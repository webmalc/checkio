def to_bin(i):
    return '{:025b}'.format(i)


def checkio(n, m):
    return sum(c1 != c2 for c1, c2 in zip(to_bin(n), to_bin(m)))


if __name__ == '__main__':
    print(checkio(1, 999999))
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(1, 999999) == 11
    assert checkio(117, 17) == 3, "First example"
    assert checkio(1, 2) == 2, "Second example"
    assert checkio(16, 15) == 5, "Third example"
