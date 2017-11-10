def _check_rows(matrix):
    stack = {}
    for row_id, row in enumerate(matrix):
        for col_id, el in enumerate(row):
            try:
                if row[col_id + 1] == el:
                    id = '{}_{}'.format(row_id, el)
                    stack[id] = stack.get(id, 1) + 1
            except IndexError:
                pass
    return bool([i for i in stack.values() if i > 3])


def _rows(matrix):
    return [[c for c in r] for r in matrix]


def _cols(matrix):
    return zip(*matrix)


def _backward_diagonals(matrix):
    b = [None] * (len(matrix) - 1)
    matrix = [b[i:] + r + b[:i] for i, r in enumerate(_rows(matrix))]
    return [[c for c in r if c is not None] for r in _cols(matrix)]


def _forward_diagonals(matrix):
    b = [None] * (len(matrix) - 1)
    matrix = [b[:i] + r + b[i:] for i, r in enumerate(_rows(matrix))]
    return [[c for c in r if c is not None] for r in _cols(matrix)]


def checkio(matrix):
    variants = [
        matrix,
        _cols(matrix),
        _forward_diagonals(matrix),
        _backward_diagonals(matrix),
    ]
    return any(map(_check_rows, variants))
