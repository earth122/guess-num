import random # standard library 標準函式庫 random 為module模組
r = random.randint(1, 100) # randint 為函式
count = 0
while True:
	count += 1 # count = count + 1 的快寫法
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')