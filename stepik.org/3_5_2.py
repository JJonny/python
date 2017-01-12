import csv

d = dict()
with open('Crimes.csv') as f:
	reader = csv.DictReader(f)

	
	for row in reader:
		
		date = row['Date'][6:10]
		t = row['Primary Type']
		
		val = 1
		try:
			if '2015' in date:
				if t in d.keys():
					d[t] += 1
				else:
					d[t] = val
		except:
			print('EEEEERR')
			print(d)
			break
print(d)


