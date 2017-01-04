import subprocess
import sys


def checkPathesFromEnvVar(substring_path):
	proc = subprocess.Popen('SET', shell=True, stdout=subprocess.PIPE)
	res = proc.communicate()
	ret_list = list()
	if proc.returncode:
		print(res[1])
	else:	
		ls = str(res[0]).split(';')	
		for path in ls:
			if substring_path in path:
				ret_list.append(path) 

		return ret_list


def printResult(ret_list):	
	for val in ret_list:
		print(val)		


if __name__=='__main__':	
	print(len(sys.argv))
	if len(sys.argv) > 1:
		pathes = checkPathesFromEnvVar(sys.argv[1])
		printResult(pathes)
		i = input()
	else:
		pass
