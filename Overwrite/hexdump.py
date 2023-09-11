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

if __name__ == "__main__"

    exehandle = open("Test.exe",'rb+')
    exedata = exehandle.read()

    print (dump(exedata))
