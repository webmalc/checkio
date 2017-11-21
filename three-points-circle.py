def checkio(data):
    x, y, z = [complex('{}+{}j'.format(x[0], x[1])) for x in eval(data)]
    w = z - x
    w /= y - x
    c = (x - y) * (w - abs(w)**2) / 2j / w.imag - x
    return '(x{:.3g})^2+(y{:.3g})^2={:.3g}^2'.format(
        *[round(v, 2) for v in (c.real, c.imag, abs(c + x))])
