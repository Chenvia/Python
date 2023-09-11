class FileScrape():

    """

    \Windows\WiFi\Secrets\

    Module returns all saved WiFi profiles and their corresponding keys.

    Retrives information from a Windows system file:

        C:\ProgramData\Microsoft\Wlansvc\Profiles\Interfaces\<InterfaceName>\<UnknownGUID>.xml

        This file has read permissions for Everyone, as such does not require elevation.
        
    """

    def __init__(self):

        from os import getcwd

        self.cwd = getcwd()
        self.keys = []
        self.file_contents()
        

    def file_contents(self):

        """

        Extracts all pertinent information from the files.

        """

        from os import listdir, chdir, getcwd

        PATH = 'C:\ProgramData\Microsoft\Wlansvc\Profiles\Interfaces'
        interface_guids = listdir(PATH)

        for x in range(0, len(interface_guids)):
            interface_guids[x] = self.adapter_guid(interface_guids[x])

        for interface in interface_guids:
            chdir('%s\%s' % (PATH, interface[1]))

            with open(listdir(getcwd())[0], 'r') as doc:
                data = doc.read()
                doc.close()

                self.ssid = self.find_data(data, 'name')[0]
                self.auth = self.find_data(data, 'authentication')[0]
                self.encrypt = self.find_data(data, 'encryption')[0]
                self.key_type = self.find_data(data, 'keyType')[0]
                self.keys.append((self.ssid, self.find_data(data, 'keyMaterial')[0]))

        chdir(self.cwd)

    def find_data(self, data, tag):

        """
        Function to find data between two XML tags.

            e.g - <data>This data will be returned!</data>s
        
        """

        from re import compile as cmpile
        from re import findall

        exp = cmpile("<%s>(\S+)<\/%s>" % (tag, tag))

        return exp.findall(data)
            
    def adapter_guid(self, interface_guid):

        """
        Resolves adapter GUID's to their human readable names

        """

        from winreg import HKEY_LOCAL_MACHINE, KEY_READ
        from winreg import ConnectRegistry, OpenKey, QueryValueEx, QueryInfoKey, EnumValue

        reg = ConnectRegistry(None, HKEY_LOCAL_MACHINE)
        reg_key = OpenKey(reg, r'SYSTEM\CurrentControlSet\Control\Network\{4d36e972-e325-11ce-bfc1-08002be10318}', KEY_READ)

        try:
            reg_subkey = OpenKey(reg_key, interface_guid + r'\Connection')
            return (QueryValueEx(reg_subkey, 'Name')[0].encode('ascii'), interface_guid)
        except:
            return None

    def get_keys(self):

        return self.keys

    def __str__(self):

        return "SSID: %s, Authentication Type: %s, Encryption Scheme: %s, Key Type: %s" % (self.ssid, self.auth, self.encrypt, self.key_type)


    

if __name__ == '__main__':

    test = FileScrape()
    print(test)
    print(test.get_keys())
