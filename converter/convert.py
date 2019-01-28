from pip._vendor.msgpack.fallback import xrange


def arabic_to_roman(arabic_number):
    units = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thousands = ["", "M", "MM", "MMM", "MMMM"]
    t = thousands[int(arabic_number) // 1000]
    h = hundreds[int(arabic_number) // 100 % 10]
    te = tens[int(arabic_number) // 10 % 10]
    u = units[int(arabic_number) % 10]

    roman = t + h + te + u

    return str(roman)


# def roman_to_arabic(roman_number):
#    numerals = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
#    arabic = 0
#    last_value = 0
#    try:
#        for value in (numerals[c] for c in reversed(roman_number.upper())):
#            v = (value, -value)[value < last_value]
#            print('{:6} += {:5}  <== cur, prev = {}, {}'.format(arabic, v, value, last_value))
#            arabic += (value, -value)[value < last_value]
#            last_value = value
#    except:
#        arabic = 0
#    return str(arabic)

def roman_to_arabic(roman_number):
    digit = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    arabic = 0
    for d in xrange(len(roman_number)):
        try:
            if digit[roman_number[d]] < digit[roman_number[d + 1]]:
                arabic -= digit[roman_number[d]]
            else:
                arabic += digit[roman_number[d]]
        except IndexError:
            arabic += digit[roman_number[d]]
    return str(arabic)
