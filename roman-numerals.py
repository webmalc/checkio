from collections import OrderedDict


def checkio(num):

    roman = OrderedDict()
    roman[1000] = "M"
    roman[900] = "CM"
    roman[500] = "D"
    roman[400] = "CD"
    roman[100] = "C"
    roman[90] = "XC"
    roman[50] = "L"
    roman[40] = "XL"
    roman[10] = "X"
    roman[9] = "IX"
    roman[5] = "V"
    roman[4] = "IV"
    roman[1] = "I"

    def roman_num(val):
        for r in roman.keys():
            x, y = divmod(val, r)
            yield roman[r] * x
            val -= (r * x)
            if val > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])