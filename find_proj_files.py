import os

def getAllProjFiles(path, file_mask):
	for root, dirs, files in os.walk(path):
		for f in files:			
			if file_mask in f:
				print(os.path.join(root, f))
				


getAllProjFiles('c:\\Program Files', '.dsm')
