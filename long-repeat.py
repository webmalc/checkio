def long_repeat(line):
    s = {}
    for k, c in enumerate(line):
        if not k or line[k - 1] != c:
            s[c] = 1
        else:
            s[c] += 1

    return s[max(s, key=s.get)] if s else 0


if __name__ == '__main__':
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    print('"Run" is good. How is "Check"?')
