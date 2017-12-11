import time
import datetime
import vk


session = vk.AuthSession(app_id='5449373', user_login='@.ru', user_password='', scope='messages')
api = vk.API(session)

values = {}
last_mess = 0

def write_msg(user_id, s):	
	print('user:', user_id)
    api.messages.send(user_id='2202824', message=s)


while True:
    response = api.messages.get(offset=0, count=1, time_offset=10)        
    print(datetime.datetime.now() , response)
    last_mess = response[0]

    if len(response) > 1:
	    if '__mag__' == response[1]['body']:
	        write_msg(response[1]['uid'], 'Местоположение магазина!')

    time.sleep(11)


