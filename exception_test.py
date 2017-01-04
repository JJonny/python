'''some exception test'''


def test_func(val):
	res = 'error'
	try:		
		res = val / 0
	except ZeroDivisionError as e:
		print('ups:', e)

	return res

r = test_func(5)
