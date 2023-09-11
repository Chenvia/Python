from PySvc import PySvc

class TestSvc(PySvc):

    _svc_name_ = "SecretsDecrypter"
    _svc_display_name_ = "Elevated SYSTEM decrypter"
    _svc_description_ = "This service runs as SYSTEM to decrpt secrets."

    def uncrypt(self, data):
        
        from binascii import unhexlify
        from crypt import uncrypt

        return uncrypt(unhexlify(data))[1].encode('ascii')

    def main(self):

        from win32event import WAIT_OBJECT_0, WaitForSingleObject
        from FileMethod import FileScrape

        file_module = FileScrape()
        result = "%s\n\n\tNetwork Key:\t%s" % (file_module, uncrypt(file_module.get_keys()[0][1]))

        with open('C:\\test.dat', 'w+')  as log_file:
            log_file.write(result)
            log_file.flush()
            log_file.close()

        rc = None 
        while rc != WAIT_OBJECT_0:  
            rc = WaitForSingleObject(self.hWaitStop, 5000) 
        
            

if __name__ == '__main__':

    from win32serviceutil import HandleCommandLine

    HandleCommandLine(TestSvc) 
