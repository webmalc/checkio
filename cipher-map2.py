def recall_password(cipher_grille, ciphered_password):
    result = ''
    cipher_list = [list(x) for x in cipher_grille]
    for r in range(0, 4):
        for k, row in enumerate(cipher_list):
            for i in [i for i, x in enumerate(row) if x == 'X']:
                result += ciphered_password[k][i]
        cipher_list = list(zip(*cipher_list[::-1]))
    return result


if __name__ == '__main__':
    assert recall_password(
        ('X...',
         '..X.',
         'X..X',
         '....'),
        ('itdf',
         'gdce',
         'aton',
         'qrdi')) == 'icantforgetiddqd', 'First example'

    assert recall_password(
        ('....',
         'X..X',
         '.X..',
         '...X'),
        ('xhwc',
         'rsqx',
         'xqzz',
         'fyzr')) == 'rxqrwsfzxqxzhczy', 'Second example'
