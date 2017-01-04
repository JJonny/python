import sys

sys.stdin = open('input_2_1.txt', 'r')
#sys.stdin = open('11.txt', 'r')

namespace = dict()

n = int(input())
for i in range(n):
	line = input()
	if ':' not in line:
		namespace[line] = ''
	else:
		exc, pred_exc  = line.split(' : ')		
		namespace[exc] = pred_exc

	# генерация листа приоритеов наследования

def find_all_paths(ns, ex_class, path=[]):  
	if ex_class == '':
		return path
	path.append(ex_class)	
	if ex_class in ns.keys():		
		node = ns[ex_class]
		if node not in path:
			newpath = find_all_paths(ns, node, path)
			if newpath: 
				return newpath
	return path




m = int(input())
cur_excp_list = []
out = []
for i in range(m):
	cur_item = input()
	if cur_item not in cur_excp_list:
		cur_excp_list.append(cur_item)
	#print('cur_item//', cur_item)

	path = []	
	ret = find_all_paths(namespace, cur_item, path)		
	#print('ret//', ret)	
	#print('Current list//:',cur_excp_list)
	for cl in ret[1:]:
		if cl in cur_excp_list:			
			out.append(cur_item)

	#print()			


for i in out:
	print(i)
print('\n',namespace)
print(cur_excp_list)
