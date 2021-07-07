import hashlib




def read_file_hash(file_object):
    while True:
        data = file_object.read()
        data_hach = hashlib.md5(b"f'{data}'").hexdigest()
        if not data:
            break
        yield data_hach


with open('text.txt') as f:
    for b in read_file_hash(f):
        print(b)