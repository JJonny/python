import sys

sys.stdin = open('11.txt', 'r')

namespace = dict()

n = int(input())
for i in range(n):
 	line = input()
 	if ':' not in line:
 		namespace[line] = []
 	else:
 		exc, pred_exc  = line.split(' : ')		
 		namespace[exc] = pred_exc.split()


for k,v in namespace.items():
	print(k,v)


itr = 0;

def find_all_paths(start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if start not in namespace.keys():
        return []
    paths = []
    for node in namespace[start]:
        if node not in path:
            newpaths = find_all_paths(node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths




m = int(input())
cur_class_list = []
for i in range(m):
	cur_class = input()
	if cur_class not in cur_class_list:
		cur_class_list.append(cur_class)	
	path=[]	
	for ii in namespace.keys():
		ret = find_all_paths(cur_class, ii, path)			
		print(ii, cur_class, ret)
# h
# f
# k
# c
# j
# g
# e
