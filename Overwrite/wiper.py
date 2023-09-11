from hexdump import dump
import string, random, os


def fixedpass(fname, seq):

    print("\n\tBefore")
    fileobj = open(fname, 'rb+')
    fcontents = fileobj.read()
    print(dump(fcontents))
    print("File Size: " + str(len(fcontents)) + " bytes\n")
    fileobj.close()
    flength = len(fcontents)
    
    dlength = 0
    while dlength < flength:
        dlength += 3
    dpass = (seq * dlength)[:flength]

    newfile = open(fname, 'rb+')
    newfile.seek(0)
    newfile.truncate()
    newfile.write(dpass)
    newfile.close()
    print("\n\tAfter")
    print(dump(open(fname,'rb+').read()))
    print("File Size: " + str(len(open(fname,'rb+').read())) + " bytes")
    return dpass

def randpass(fname):

    fileobj = open(fname, 'rb+')
    fcontents = fileobj.read()
    flength = len(fcontents)
    print("\n\tBefore")
    print(dump(fcontents))
    print("File Size: " + str(flength) + " bytes\n")

    dpass = ''.join( random.SystemRandom().choice(string.ascii_letters + string.digits + string.punctuation) for i in range(0,flength))
    
    newfile = open(fname, 'rb+')
    newfile.seek(0)
    newfile.truncate()

    newfile.write(dpass)
    newfile.close()
    print("\n\tAfter")
    print(dump(open(fname,'rb+').read()))
    print("File Size: " + str(len(open(fname,'rb+').read())) + " bytes")
    return dpass

def verify(data,fname):

    fileobj = open(fname, 'rb+')
    fdata = fileobj.read()
    fileobj.close()
    if data == fdata:
        return True
    else:
        return False
    

def B_HMG_IS5_B(fname):
    
    """ British HMG IS5 - Baseline (1 pass + 1 verification pass)
    This baseline scheme allows the data sectors in the storage device to be overwritten with
    zeroes. This wiping method also does a verification pass to ensure that the data written is
    correct."""

    verpass = fixedpass(fname, "\x00")
    if verify(verpass,fname) != True:
        raise ValueError("Expected Values of file were not found when opening!")
    os.delete(fname)


def B_HMG_IS5_E(fname):

    """British HMG IS5 - Enhanced (3 passes + 1 verification pass)
    This enhanced scheme is a three pass overwriting algorithm. In the first pass, it overwrites
    all the data sectors in the storage device with 0x00. In the second pass, it overwrites the
    entire data sectors again with 0xFF. In the last pass, it overwrites all the data sectors in the
    storage device with pseudo-random numbers. This wiping method also does a verification
    pass after the third pass to ensure that the data overwritten are correct"""

    fixedpass(fname, "\x00")
    fixedpass(fname, "\xFF")
    verpass = randpass(fname)
    if verify(verpass,fname) != True:
        raise ValueError("Expected Values of file were not found when opening!")
    os.delete(fname)


def R_GOST_P50739_35(fname):

    
    """Russian GOST P50739-95 (2 passes)
    This Russian standard allows the data sectors in the storage device to be overwritten with a
    single pass of zeroes (0x00), followed by another pass with pseudo-random numbers."""

    fixedpass(fname, "\x00")
    verpass = randpass(fname)
    if verify(verpass,fname) != True:
        raise ValueError("Expected Values of file were not found when opening!")
    os.delete(fname)
    

def US_DoD_5220_22_M(fname):

    """U.S. Standard, DoD 5220.22-M (3 passes)
    The National Industrial Security Program Operating Manual, issued to the US Department of
    Defense, Department of Energy, and other US government agencies specifies standards for
    the clearing, and sanitising of data classified as confidential, secret. U.S. Department of Defense specifies three passes extended character rotation overwrite
    algorithm in the DoD 5220.22-M specification. This Total Privacy shredding method
    conforms to these overwriting standards as well as method 'd' of the Cleaning and Sanitation
    Matrix (DoD, 2006).
    """
    
    randpass(fname)
    randpass(fname)
    randpass(fname)
    os.delete(fname)


def C_RCMP_DSX(fname):

    """Canadian RCMP DSX Method (3 passes + 3 verification passes)
    The DSX method is a three pass overwriting algorithm. In the first pass, it overwrites all the
    data sectors in the storage device with zeroes. In the second pass, it overwrites the entire data
    sectors again with ones. In the third pass, it overwrites all the data sectors in the storage
    device with pseudo-random numbers. After each pass, the values overwritten in the data
    sectors are verified to ensure integrity (RCMP, 2003)."""    

    verpass = fixedpass(fname,"\x00")
    if verify(verpass,fname) != True:
        raise ValueError("Pass 1/3 - Expected Values of file were not found when opening!")
    verpass = fixedpass(fname,"\x01")
    if verify(verpass,fname) != True:
        raise ValueError("Pass 2/3 - Expected Values of file were not found when opening!")
    verpass = randpass(fname)
    if verify(verpass,fname) != True:
        raise ValueError("Pass 3/3 - Expected Values of file were not found when opening!")
    os.delete(fname)


def C_RCMP_TSSIT_OPS_11(fname):
    
    """Canadian RCMP TSSIT OPS-II (7 passes + 1 verification pass)
    This method is a seven passes overwriting algorithm with three alternating patterns of zeroes
    and ones followed by the last pass with random characters. This wiping method also does a
    verification pass to ensure that the data overwritten in the final pass is correct."""

    fixedpass(fname, "\x00")
    fixedpass(fname, "\x01")
    fixedpass(fname, "\x00")
    fixedpass(fname, "\x01")
    fixedpass(fname, "\x00")
    fixedpass(fname, "\x01")
    verpass = randpass(fname)
    if verify(verpass,fname) != True:
        raise ValueError("Expected Values of file were not found when opening!")
    os.delete(fname)


def G_VSITR(fname):

    """German VSITR (7 passes)
    Similar to previous method, the German standard overwrites each data sector in the storage
    device with three alternating patterns of zeroes and ones, followed by the seventh pass with
    random character. However, no verification on the overwritten data is needed."""

    fixedpass(fname, "\x00")
    fixedpass(fname, "\x01")
    fixedpass(fname, "\x00")
    fixedpass(fname, "\x01")
    fixedpass(fname, "\x00")
    fixedpass(fname, "\x01")
    verpass = randpass(fname)
    os.delete(fname)


def Bruce_Schneier(fname):

    """Bruce Schneiers Algorithm (7 passes)
    This method offers a seven pass overwriting algorithm. The first pass with all ones, the
    second pass with all with zeroes and then five more passes with a cryptographically secure
    pseudo-random sequence (Schneier, 1996)."""

    fixedpass(fname, "\x01")
    fixedpass(fname, "\x00")
    for i in range(0,5):
        randpass(fname)
    os.delete(fname)

def Gutmann(fname):

    for i in range(0,4):
        randpass(fname)
    fixedpass(fname,"\x55\x55\x55")
    fixedpass(fname,"\xAA\xAA\xAA")
    fixedpass(fname,"\x92\x49\x24")
    fixedpass(fname,"\x49\x24\x92")
    fixedpass(fname,"\x24\x92\x49")
    fixedpass(fname,"\x00\x00\x00")
    fixedpass(fname,"\x11\x11\x11")
    fixedpass(fname,"\x22\x22\x22")
    fixedpass(fname,"\x33\x33\x33")
    fixedpass(fname,"\x44\x44\x44")
    fixedpass(fname,"\x55\x55\x55")
    fixedpass(fname,"\x66\x66\x66")
    fixedpass(fname,"\x77\x77\x77")
    fixedpass(fname,"\x88\x88\x88")
    fixedpass(fname,"\x99\x99\x99")
    fixedpass(fname,"\xAA\xAA\xAA")
    fixedpass(fname,"\xBB\xBB\xBB")
    fixedpass(fname,"\xCC\xCC\xCC")
    fixedpass(fname,"\xDD\xDD\xDD")
    fixedpass(fname,"\xEE\xEE\xEE")
    fixedpass(fname,"\xFF\xFF\xFF")
    fixedpass(fname,"\x92\x49\x24")
    fixedpass(fname,"\x24\x92\x49")
    fixedpass(fname,"\x24\x92\x49")
    fixedpass(fname,"\x6D\xB6\xDB")
    fixedpass(fname,"\xB6\xDB\x6D")
    for i in range(0,4):
        randpass(fname)
    os.delete(fname)


if __name__ == "__main__":

    Gutmann('test.txt')
