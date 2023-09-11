def luhn(sequence):
    
    digits = [int(digit) for digit in str(sequence)] # converts a full string of nums to a list comp of individual numbers
    odd = digits[-1::-2] # string stepping (-1) indicates last item in list (-2) means to travel back another 2
    even = digits[-2::-2]
    checksum = 0
    checksum += sum(odd)
    evenmod = []
    for digit in even:
        if digit * 2 > 9:
            digit = digit * 2
            digit = int(str(digit)[0]) + int(str(digit)[1])
        else:digit = digit * 2
        evenmod.append(digit)
    checksum += sum(evenmod)
    if checksum % 10 == 0:
        return True
    else:
        return False


print(luhn(378282246310005))
print(luhn(111111111111111))
print(luhn(4751290083628479))
print(luhn(5573485043994670))


