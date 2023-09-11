Set of functions that allow for secure deletion of files.

Overwrite methods include:

  B HMG IS5 - Baseline - British Her Majesties Government Infosec Standard 5 Basic

    1 pass + 1 verification pass

    This baseline scheme allows the data sectors in the storage device to be overwritten with
    zeroes. This wiping method also does a verification pass to ensure that the data written is
    correct.

  B HMG IS5 - Enhanced - British Her Majesties Government Infosec Standard 5 Enhanced

    3 passes + 1 verification pass

    This enhanced scheme is a three pass overwriting algorithm. In the first pass, it overwrites
    all the data sectors in the storage device with 0x00. In the second pass, it overwrites the
    entire data sectors again with 0xFF. In the last pass, it overwrites all the data sectors in the
    storage device with pseudo-random numbers. This wiping method also does a verification
    pass after the third pass to ensure that the data overwritten are correct.

  R GOST P50739 35 - Russian Gosudarstvennyy Standart 

    2 passes
    This Russian standard allows the data sectors in the storage device to be overwritten with a
    single pass of zeroes (0x00), followed by another pass with pseudo-random numbers.

  US DoD 5220.22 M - United States Department of Defence, Defined in National Industrial Security Program Operations Manual

    3 passes
    The National Industrial Security Program Operating Manual, issued to the US Department of
    Defence, Department of Energy, and other US government agencies specifies standards for
    the clearing, and sanitising of data classified as confidential, secret. U.S. Department of Defence specifies three passes extended character rotation overwrite
    algorithm in the DoD 5220.22-M specification. This Total Privacy shredding method
    conforms to these overwriting standards as well as method 'd' of the Cleaning and Sanitation
    Matrix (DoD, 2006).

  C RCMP DSX - Canadian Royal Canadian Mounted Police

    3 passes + 3 verification passes

    The DSX method is a three pass overwriting algorithm. In the first pass, it overwrites all the
    data sectors in the storage device with zeroes. In the second pass, it overwrites the entire data
    sectors again with ones. In the third pass, it overwrites all the data sectors in the storage
    device with pseudo-random numbers. After each pass, the values overwritten in the data
    sectors are verified to ensure integrity (RCMP, 2003)

  C RCMP TSSIT OPS-II - Canadian Royal Canadian Mounted Police Technical Security Standard for Information Technology
  
    7 passes + 1 verification pass

    This method is a seven passes overwriting algorithm with three alternating patterns of zeroes
    and ones followed by the last pass with random characters. This wiping method also does a
    verification pass to ensure that the data overwritten in the final pass is correct.

  G VSITR - German VS-ITR

    7 passes

    Similar to previous method, the German standard overwrites each data sector in the storage
    device with three alternating patterns of zeroes and ones, followed by the seventh pass with
    random character. However, no verification on the overwritten data is needed.

  Bruce Schneiers Algorithm

    7 passes

    This method offers a seven pass overwriting algorithm. The first pass with all ones, the
    second pass with all with zeroes and then five more passes with a cryptographically secure
    pseudo-random sequence (Schneier, 1996).

  Gutmann 

    35 passes

    This method offers a thirty five pass overwriting system. Four random passes followed by twenty seven fixed passes
    Followed by a further four random passes. 

