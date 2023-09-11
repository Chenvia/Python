def md5hash_file(file_path):

    from hashlib import md5

    with open(file_path, 'rb') as input_file:
        data = input_file.read()
        input_file.close()

    secure_hash = md5(data)

    return secure_hash.hexdigest().upper()


if __name__ == '__main__':

    print(md5hash_file('JM'))

    
