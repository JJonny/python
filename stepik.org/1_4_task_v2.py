#n = 9
n = 15
#n = 6
'''query = [   'add global a',
			'create foo global',
			'add foo b',
			'get foo a',
			'get foo c',
			'create bar foo',
			'add bar a',
			'get bar a',
			'get bar b'
		]'''


query = [ 'add global a',
'create foo1 global',
'create foo2 global',
'create bar1 foo1',
'create bar2 foo2',
'create new1 bar1',
'create new2 bar2',
'add global b',
'add foo1 a',
'add foo2 b',
'add bar1 a',
'add bar2 b',
'add new1 a',
'add new2 b',
'get new1 b'
]

'''query = ['create foo global',
'create bar foo',
'add global a',
'add foo a',
'add bar c',
'get global c',
'bar' ]'''


namespaces = {'global' : {'parrent' : None, 'vars' : [] } } 

def getNS(dictionary, variable, ns):
	if ns in dictionary.keys():
		#print(dictionary.keys())
		d = dictionary[ns]
		#print(d)
		if var in d['vars']:
			#print('iiiii')
			return ns
		elif d['parrent'] != None:			
			parrent_ns = d['parrent']
			#print('parr:', parrent_ns)
			ret_val = getNS(dictionary, variable, parrent_ns)
			return ret_val
		else:
			#print('Ups')
			return None
	else:		
		return None



for i in range(n):    	
	cmd, nmsp, var = query[i].split()			

	if cmd == 'add':		
		namespaces[nmsp]['vars'].append(var) 		
	elif cmd == 'create':
		namespaces[nmsp] = {'parrent': var, 'vars' : []}
	elif cmd == 'get':
		print(cmd, nmsp, var)
		res = getNS(namespaces, var, nmsp)
		print(res)

for i in namespaces:
	print(i, namespaces[i])
		
			



#print('namespaces', namespaces, '\n')

