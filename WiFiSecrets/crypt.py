def uncrypt(data):

    """
    Levereges win32api CryptUnprotectData to un-encrypt data protected by win32crypt

    Returns unencrypted data.
    
    """

    from win32crypt import CryptUnprotectData

    return CryptUnprotectData(data)

def crypt(data):

    """
    Levereges win32api CryptProtectData to encrypt data with by win32crypt

    Returns encrypted data

    """

    from win32crypt import CryptProtectData

    return CryptProtectData(data)


if __name__ == '__main__':

    pass
