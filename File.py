class File():

    def __init__(self, filename):

        from os.path import isabs

        if isabs(filename):
            self.path = filename
            self.filename = self.get_base()
        else:
            self.filename = filename
            self.path = self.get_absolute()

        try:
            self.file_handle = self.get_file_handle(self.path)
        except:
            self.folder_handle = self.get_file_handle(self.path)

    def get_UID(self):

        from win32security import GetFileSecurity, OWNER_SECURITY_INFORMATION, LookupAccountSid

        sd = GetFileSecurity(self.filename, OWNER_SECURITY_INFORMATION)
        owner_sid = sd.GetSecurityDescriptorOwner()
        name, domain, type = LookupAccountSid(None, owner_sid)

        return "%s\\%s" % (domain, name)

    def get_modify_time_os(self):

        from os.path import getmtime
        from os import stat

        status = stat(self.path)

        return getmtime(self.path)

    def get_absolute(self):

        from os.path import abspath

        return abspath(self.filename)

    def dir_info(self, path):

        from os.path import join, abspath
        from os import pardir

        return abspath(join(path, pardir))

    def get_directory(self):

        return self.dir_info(self.get_absolute())
        
    def get_parent_dir(self):

        return self.dir_info(self.get_directory())
    

    def get_base(self):

        from os.path import basename

        return basename(self.path)


    def get_file_handle(self,file_name):

        from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING
        from win32file import CreateFile

        return CreateFile(file_name, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, 0, 0)

    def get_folder_handle(self, file_name):

        from win32file import GENERIC_READ, GENERIC_WRITE, OPEN_EXISTING, FILE_FLAG_BACKUP_SEMANTICS
        from win32file import CreateFile

        return CreateFile(file_name, GENERIC_READ | GENERIC_WRITE, 0, None, OPEN_EXISTING, FILE_FLAG_BACKUP_SEMANTICS, 0)

    def close(self):

        from win32file import CloseHandle

        CloseHandle(self.file_handle)

    def get_create_time(self):

        from win32file import GetFileTime
        from time import ctime

        create_time, anon, anon1 = GetFileTime(self.file_handle)
        return ctime(int(create_time))

    def get_access_time(self):

        from win32file import GetFileTime
        from time import ctime

        anon, access_time, anon1 = GetFileTime(self.file_handle)
        return ctime(int(access_time))

    def get_modify_time_win32(self):

        from win32file import GetFileTime
        from time import ctime

        anon, anon1, modify_time = GetFileTime(self.file_handle)
        return ctime(int(modify_time))

    def get_all_times(self):

        from win32file import GetFileTime
        from time import ctime

        create_time, access_time, modify_time = GetFileTime(self.file_handle)
        return ctime(int(create_time)), ctime(int(access_time)), ctime(int(modify_time))

    def convert_time(self, time):

        from time import localtime, mktime, strptime, localtime
        from pywintypes import Time

        time_format = "%d.%m.%Y %H:%M:%S"
        now = localtime()

        structured_format = localtime(mktime(strptime(time, time_format)))
        file_time = Time(mktime(structured_format) + 3600 * (now.tm_isdst - structured_format.tm_isdst))

        return file_time


    def set_all_timestamps(self, create_time, accessed_time, modified_time):

        from win32file import SetFileTime

        create_time = self.convert_time(create_time)
        accessed_time = self.convert_time(accessed_time)
        modified_time = self.convert_time(modified_time)
        
        SetFileTime(self.file_handle, create_time, accessed_time, modified_time)

    def bit_by_bit_copy(self, output_location, filename=None):

#       #timestamps are updated on input file when opened

        from win32file import CopyFile

        if not filename:
            filename = self.filename

        outfile = "%s\\%s" % (output_location, filename)

        self.close()
        CopyFile(self.path, outfile, 1)
        self.file_handle = self.get_file_handle(self.path)

        timestamps = self.get_all_times()

        print(outfile)
        print(timestamps)
        
        out = File(outfile)
        out.set_all_timestamps(timestamps[0], timestamps[1], timestamps[2])

    def time_format(self, time):

        year = time.split(" ")[4] 

if __name__ == '__main__':

    test = File('test.txt')
    
    print(test.path)
    print(test.get_directory())
    print(test.get_parent_dir())
    
    print(test.get_UID())
    
    print(test.get_all_times())
    test.set_all_timestamps("01.03.2000 00:00:00", "01.03.2000 00:00:00", "01.03.1980 00:00:00")
    print(test.get_all_times())
    
    test.bit_by_bit_copy("test2.txt")
    test.close()
