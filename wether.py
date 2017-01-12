import requests

with open('log.txt', 'a') as f:

	params = {
		'q' : 'Kyiv',
		'appid' : '30ae1c87f0c67c9bbbd4673539cf371d',
		'units' : 'metric'
	}
	
	api_req = 'http://api.openweathermap.org/data/2.5/forecast'
	try:
		r = requests.get(api_req, params=params)

		print(r.status_code)		
		# f.write(r.text + '\n')
		data = r.json()
		print(data['city']['name'])
		for i in data['list']:			
			print(i['dt_txt'], i['main']['temp'])
		

	except BaseException as er:		
			f.writelines('==>' + str(er) + '\n')
			print('Error', er)
