import sys

sys.stdin = open('11.txt', 'r')
#sys.stdin = open('11.txt', 'r')

namespace = dict()

n = int(input())
for i in range(n):
 	line = input()
	if ':' not in line: 
		namespace[line] = []
	else:
		exc, pred_exc  = line.split(' : ')		
		namespace[exc] = pred_exc.split()

print(namespace)


def find_all_paths(ns, cur_class, cur_class_list=[], paretns=[]):  
	# if cur_class == '':
	# 	return paretns
	# paretns.append(cur_class)	
	# if cur_class in ns.keys():		
	# 	node = ns[cur_class]
	# 	if node not in paretns:
	# 		newpath = find_all_paths(ns, node, paretns)
	# 		if newpath: 
	# 			return newpath
	# return paretns

	for cl in paretns:
	if pred in paretns:
		return 'Yes'
	else:		
		for sub_cl in paretns: #rel[obj]['predok']:
			ret_val = "No"
			if obj == sub_cl:
				return 'No'
			elif sub_cl in rel.keys(): 
				ret_val = is_predok(pred, sub_cl, rel[sub_cl]['predok'])
			return ret_val	




m = int(input())
cur_class_list = []
for i in range(m):
	cur_class = input()
	if cur_class not in cur_class_list:
		cur_class_list.append(cur_class)	
	
	if cur_class in namespace.keys():
		ret = find_all_paths(namespace, cur_class, cur_class_list, namespace[cur_class])			

	

