import subprocess
#import sys


def checkPathesFromEnvVar(cmd):
	proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
	res = proc.communicate()
	print(res[0].decode('utf-8'))
	if proc.returncode:
		print(res[1])


#checkPathesFromEnvVar('calc')
#checkPathesFromEnvVar('regedit')
checkPathesFromEnvVar('sqlite_index.py')
