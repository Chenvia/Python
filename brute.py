def rarfile(input_file, dictionary):

        import rarfile
        
	"""
	Rarfile password cracker using a brute-force dictionary attack
	"""
	rarfilename = input_file

	password = None
	rar_file = rarfile.RarFile(rarfilename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				rar_file.extractall(pwd=password)
				password = 'Password found: %s' % password
			except:
                                count += 1
				print('Fail: %s' % password)
	print(password)


def zipfile(input_file, dictionary):

        import zipfile
        
	"""
	Zipfile password cracker using a brute-force dictionary attack
	"""
	zipfilename = input_file

	password = None
        zip_file = zipfile.ZipFile(zipfilename)
	with open(dictionary, 'r') as f:
		for line in f.readlines():
			password = line.strip('\n')
			try:
				zip_file.extractall(pwd=password)
				password = 'Password found: %s' % password
			except:
				print(Fail: %s' % password)
	print(password)

