#create function for beatuifying results and returning to console
# possible create cli tool with arg parse

class FileIdentifier():

    def __init__(self):

        self.prepare_dictionary()
        self.results = []

    def prepare_dictionary(self):

        from xlrd import open_workbook

        dictionary = {}

        workbook = open_workbook("headers.xlsx")
        sheet = workbook.sheet_by_index(0)
        rows = sheet.nrows

        for i in range(rows):
            
            cell_value_class = sheet.cell(i,1).value
            cell_value_id = "%s" % sheet.cell(i,0).value
            dictionary[cell_value_id] = cell_value_class

        self.dictionary = dictionary

    def set_file_path(self, file_path):
        self.file_path = file_path
        self.get_file_contents()

    def get_file_contents(self):

        with open(self.file_path, 'r', encoding='ansi') as file_handle:

            data = file_handle.read()
            file_handle.close()

        self.data = data
    

    def get_file_start(self):

        signature = self.data[:15]

        signature = " ".join("{:02x}".format(ord(c)) for c in signature)
        signature = signature[:11].upper()

        return signature

    def check_signatures(self):
        
        signature = self.get_file_start()

        for i in self.dictionary:        
            if i in signature:
                return "%s - Match %s file - %s\t%s" % (self.file_path, self.dictionary[i].upper(), signature, i)
        

    def check_xml(self):

        #regex matches to most text 

        from re import compile as re_compile
        from re import search

        expression = re_compile(r'<style type=\"text/css\">[\s\S]*</style>')

        if search(expression, self.data):
            return("%s - Match CSS File - <style type=\"text/css\">DATA</style>" % self.file_path)

        expression = re_compile(r'<html>[\s\S]*</html>')

        if search(expression, self.data):
            return("%s - Match HTML File - <html>DATA</html>" % self.file_path)

    def md5hash_file(self, file_path):

        from hashlib import md5

        with open(file_path, 'rb') as input_file:
            data = input_file.read()
            input_file.close()

        secure_hash = md5(data)
    
        return "MD5 Hash - %s" % secure_hash.hexdigest().upper()

    def check_file(self, file_path):

        self.set_file_path(file_path)
        self.results = []

        hit = test.check_signatures()
        if hit:
            self.results.append(hit)
            self.results.append(self.md5hash_file(file_path))
            return self.results

        hit = test.check_xml()
        if hit:
            self.results.append(hit)
            self.results.append(self.md5hash_file(file_path))
            return self.results

        return self.results

if __name__ == '__main__':    
    
    test = FileIdentifier()

    while 1:
        try:
            file_path = input("File Path to Test: ")
            for result in test.check_file(file_path):
                print(result)
        except KeyboardInterrupt:
            print("Quitting!")



    

    
