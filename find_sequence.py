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


# print()
# stack = {i: {} for i in ['v', 'h', 'dr', 'dl']}
# for row_id, row in enumerate(matrix):
#     for col_id, el in enumerate(row):
#         try:
#             if row[col_id + 1] == el:
#                 stack['h'][row_id] = stack['h'].get(row_id, 0) + 1

#             if matrix[row_id + 1][col_id] == el:
#                 stack['v'][col_id] = stack['v'].get(col_id, 0) + 1

#             # if matrix[row_id + 1][col_id + 1] == el:
#             #     stack['dr'][row_id] = stack['dr'].get(col_id + row_id,
#             #                                           0) + 1
#             # if matrix[row_id + 1][col_id - 1] == el:
#             #     stack['dl'][row_id] = stack['dl'].get(col_id + row_id,
#             #                                           0) + 1
#         except IndexError:
#             pass

# return bool(list(filter(lambda x: x > 2, \
#                         chain(*[m.values() for m in stack.values()]))))

if __name__ == '__main__':
    assert checkio(
        [[2, 7, 6, 2, 1, 5, 2, 8, 4, 4], [8, 7, 5, 8, 9, 2, 8, 9, 5, 5], [
            5, 7, 7, 7, 4, 1, 1, 2, 6, 8
        ], [4, 6, 6, 3, 2, 7, 6, 6, 5, 1], [2, 6, 6, 9, 8, 5, 5, 6, 7, 7],
         [9, 4, 1, 9, 1, 3, 7, 2, 3, 1], [5, 1, 4, 3, 6, 5, 9, 3, 4, 1],
         [6, 5, 5, 1, 7, 7, 8, 2, 1, 1], [9, 5, 7, 8, 2, 9, 2, 6, 9, 3],
         [8, 2, 5, 7, 3, 7, 3, 8, 6, 2]]) is False
