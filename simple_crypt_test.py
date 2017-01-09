from simplecrypt import encrypt, decrypt


with open('./other_files/encrypted.bin', 'rb') as inp:
	encrypted = inp.read()