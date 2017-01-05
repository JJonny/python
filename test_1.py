tx = 'ÄËß ÏÐÎÂÅÐÊÈ ÊÎÍÂÅÐÒÀÖÈÈÎÊÎÍ×ÀÒÅËÜÍÛÉ ÐÀÑ×ÅÒ ÏÎ ÇÏ SDFSD SFDFSD  ÍÀ 3014000097401/234-4561111ÎÊÎÍ×ÀÒÅËÜÍÛÉ ÐÀÑ×ÅÒ ÏÎ ÇÏ SDFSD SFDFSD  ÍÀ 3014000097401/234-4561111'

print(tx[93:])
print(tx[:93])


def createGenerator():
	for x in range(1,11):
		if x % 2 == 0:
			print(x)
			yield x	


#gener = createGenerator()

for i in createGenerator():
	print('for',i)

