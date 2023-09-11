"""
    ISO_7064_mod_97_10
        - Validates IBAN's
"""

def generate_sum(number):

    number = (98 - (number * 100 % 97) % 97)
    return number

def validate_sum(number):

    if number % 97 == 1:
        return True
    else:
        return False

print(generate_sum(123456))
print(validate_sum(12345676))

print("%d%d" % (generate_sum(9005), generate_sum(8428)))
