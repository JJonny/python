import sys

sys.stdin = open('input.txt', 'r')

graph = {} #{ obj : base_list[] }

n = int(input())
for i in range(n):		
	i_n = str(input())
	if ':' in i_n:
		obj, pred = i_n.split(' :')
		graph[obj] = pred.split()
	else:					
		graph[i_n] = list(i_n)


for k in graph:
	print(k, graph[k])

'''def is_predok(pred, obj, pred_ls):	
		if pred in pred_ls:
			return 'Yes'
		else:		
			for sub_cl in pred_ls: #rel[obj]['predok']:
				ret_val = 'No'
				if obj == sub_cl:
					return 'No'
				elif sub_cl in rel.keys(): 
					ret_val = is_predok(pred, sub_cl, rel[sub_cl]['predok'])
				return ret_val'''

def is_predok(graph, start, end):
	if start not in graph.keys():
		return 'No'
	if end in graph[start]:
		return 'Yes'	
	for node in graph[start]:		
		if node == start:
			return 'No'		
		ret = is_predok(graph, node, end)
		return ret
	return 'No'

def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph.keys():
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths

q = int(input())
for i in range(q):	
	pred, obj = input().split()	
	ret = 'No'	
	if pred == obj:
		ret = 'Yes'
	else:		
		#if obj in graph.keys():				
		#ret = is_predok(graph, obj, pred)
		ret_ls = find_all_paths(graph, obj, pred)
		if len(ret_ls) > 0:
			ret = 'Yes'
		#else:
		#ret = 'No'
	print(ret)
