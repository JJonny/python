n = 15
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


'''query = [ 'add global a',
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
]'''



namespaces = {'global' : {'parrent' : None, 'vars' : [] } } 


for i in range(n):    	
	cmd, nmsp, var = query[i].split()			

	if cmd == 'add':		
		namespaces[nmsp]['vars'].append(var) 
		print(namespaces, namespaces['global']['vars'])
		
			
		
    #elif cmd == 'create':

    #elif cmd == 'get':
     
	


#print('namespaces', namespaces, '\n')

