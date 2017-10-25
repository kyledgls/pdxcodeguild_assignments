# converts digits to language



x = 375
tens_digit = x//10
ones_digit = x%10
hundreds_digit = x//100
ones = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
hundos = ['one hundred', 'two hundred', 'three hundred', 'four hundred', 'five hundred', 'six hundred', 'seven hundred',
          'eight hundred', 'nine hundred']

# print(tens_digit, ones_digit)

if x < 10:
    print(ones[ones_digit])
elif x < 20:
    print(teens[ones_digit-10])
elif x < 99:
    print(tens[tens_digit - 2], ones[ones_digit])
elif x < 999:
    print(hundos[hundreds_digit-1], ones[ones_digit-10])






