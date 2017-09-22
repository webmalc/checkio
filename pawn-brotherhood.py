import string


def safe_pawns(pawns):
    result = 0
    letters = string.ascii_letters

    def check(index):
        return letters[index] + str(k) in pawns

    for pawn in pawns:
        i = letters.index(pawn[0])
        k = int(pawn[1]) - 1
        if check(i + 1):
            result += 1
            continue
        if check(i - 1):
            result += 1
            continue
    return result


if __name__ == '__main__':
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    assert safe_pawns(["a1", "b2", "c3", "d4", "e5", "f6", "g7", "h8"]) == 7
    print(
        "Coding complete? Click 'Check' to review your tests and earn cool rewards!"
    )
