import requests
import sys
import re


sys.stdin = open('input_3_4_7.txt')

l=[]
for i in sys.stdin:	
	l.append(i)

def find_url(code):
	o = r'(?:<a.*href=)(?:\"|\')(?:http://|https://|ftp://|)([-_\.\w]*)'
	found = re.findall(o, code)		
	# if len(found) > 0:
	return found


try:
	res = requests.get('http://stackoverflow.com/questions/3641722/valid-characters-for-uri-schemes/3641782#3641782')		
	print(res.status_code)
	if res.status_code != 404:
		print(find_url(res.text))
except:
	print('e')

# for href in l:
# 	print(find_url(href))
# 	try:
# 		res = requests.get('https://stepik.org/lesson/%D0%9E%D0%B1%D0%B7%D0%BE%D1%80%D0%BD%D0%BE-%D0%BE%D0%B1-%D0%B8%D0%BD%D1%82%D0%B5%D1%80%D0%BD%D0%B5%D1%82%D0%B5-http-%D0%B7%D0%B0%D0%BF%D1%80%D0%BE%D1%81%D1%8B-html-%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D1%8B-%D0%B8-requests-24471/step/7?course=Python-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D1%8B-%D0%B8-%D0%BF%D1%80%D0%B8%D0%BC%D0%B5%D0%BD%D0%B5%D0%BD%D0%B8%D0%B5&unit=6780')		
# 		print(res.status_code)
# 		if res.status_code != 404:

# 			print(find_url(res.text))
# 	except:
# 		print('e')
