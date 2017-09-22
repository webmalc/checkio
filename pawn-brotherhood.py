def safe_pawns(pawns):
    def check(index, k):
        return chr(index) + str(int(k) - 1) in pawns

    return sum(1 if check(ord(i) + 1, k) or check(ord(i) - 1, k) else 0
               for i, k in pawns)
