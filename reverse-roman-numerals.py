def reverse_roman(roman_string):

    roman_map = (('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100),
                 ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9),
                 ('V', 5), ('IV', 4), ('I', 1))
    result = 0
    index = 0
    for n, i in roman_map:
        while roman_string[index:index + len(n)] == n:
            result += i
            index += len(n)
    return result


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert reverse_roman('VI') == 6, '6'
    assert reverse_roman('LXXVI') == 76, '76'
    assert reverse_roman('CDXCIX') == 499, '499'
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888, '3888'
