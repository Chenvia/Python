from argparse import ArgumentParser

class Parser(ArgumentParser):

    __version__ = 'Version: 1.0.2'

    """
        Add error handling for incorect privilges.
        Elevate to admin if not on -A option.

        Add version infomation to custo9j@?p screen.
        Display help message with python argparse when script is called without any arguments.
    """

    def __init__(self):
    
        from FileMethod import FileScrape
            
        admin = False
        parser = ArgumentParser()

        parser.add_argument("-A", "--admin", help="Uses the Network Shell(netsh.exe) to retrieve WiFi information, requires Administrator access but returns plaintext value.",
                            action="store_true")
        parser.add_argument("-S", "--system", help="The File Scraping method retrieves and encrypted version, encrypted with win32crypt.CryptProtectData, This can only by done by the System account that encrypted it.",
                            action="store_true")
        parser.add_argument('--version', action='version',
                        version='%(prog)s {version}'.format(version=self.__version__))
        
        args = parser.parse_args()

        if args.admin:

            from Netsh import NetworkShell
            module = NetworkShell()
            admin = True
            

        file_module = FileScrape()
            
        if not admin:

            if args.system:
                self.result = "%s\n\n\tNetwork Key:\t%s" % (file_module, self.uncrypt(file_module.get_keys()[0][1]))
            else:
                self.result = "%s\n\n\tNetwork Key:\t%s" % (file_module, file_module.get_keys()[0][1])
            
        else:
            
            from re import findall
            from re import compile as cmpile

            exp = cmpile(":\s(\S+)")
            matches = exp.findall(str(module.get_keys()))
            self.result = "%s\n\n\tNetwork Key:\t%s" % (file_module, matches[0])
        
    def run(self):
        print(self.result)

    def uncrypt(self, data):
        
        from binascii import unhexlify
        from crypt import uncrypt

        return uncrypt(unhexlify(data))[1].encode('ascii')

    def error(self, message):

        from sys import exit as sexit, stderr
        
        sys.stderr.write('error: %s\n poop' % message)
        self.print_help(stderr)
        sexit(2)

if __name__ == '__main__':

    test = Parser()
    test.run()
    
