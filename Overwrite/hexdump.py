import sys, os

def dump(src, length=8):
    FILTER=''.join([(len(repr(chr(x)))==3) and chr(x) or '.' for x in range(256)])
    N=0; result=''
    while src:
       s,src = src[:length],src[length:]
       hexa = ' '.join(["%02X"%ord(x) for x in s])
       s = s.translate(FILTER)
       result += "%04X   %-*s   %s\n" % (N, length*3, hexa, s)
       N+=length
    return result

exehandle = open("C:\\Users\\User\\Desktop\\Documents\\Python\\Resources\\Veil Evasion\\tools\\hyperion\\Term.exe",'rb+')
exedata = exehandle.read()

print exedata
#print dump(exedata)
