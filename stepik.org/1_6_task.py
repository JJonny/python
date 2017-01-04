n = 4 #int(input())
q = 4

inp = [ 'B : A',
		'A',
		'C',
		'C : A',
		'D : B C',
		'E'
		 ]


q_inp = [ 'A B',
		  'B D',
		  'C D',
		  'D A',
		  'A D',
		  'E D',
		  'C B',
		  'B C' ]
'''inp = [ 'Ccc : Ac B',
			'D : Ccc',
			'E : Ccc',
			'F : D',
			'Goblin : E',
			'H : Goblin',
			'I : H'	 ]


q_inp = [ 'Ac Ac',
			'Ac E',  
			'E F',			
			'B Goblin',  
			'Ac I'  ]'''

rel = {} #{ obj : base_list[] }

for i_n in inp:		
	if ':' in i_n:
		obj, pred = i_n.split(' :')
		rel[obj] = { 'predok' : pred.split() }
	else:					
		rel[i_n] = { 'predok' : list(i_n) }


for k in rel:
	print(k, rel[k])

def is_predok(pred, obj, pred_ls):	
	if pred in pred_ls:
		return 'Yes'
	else:		
		for sub_cl in pred_ls: #rel[obj]['predok']:
			ret_val = 'No'
			if obj == sub_cl:
				return 'No'
			elif sub_cl in rel.keys(): 
				ret_val = is_predok(pred, sub_cl, rel[sub_cl]['predok'])
			return ret_val	

for q_n in q_inp:
	pred, obj = q_n.split()	
	ret = 'No'	
	if pred == obj:
		ret = 'Yes'
	else:		
		if obj in rel.keys():				
			ret = is_predok(pred, obj, rel[obj]['predok'])
		else:
			ret = 'No'
	print(ret)
