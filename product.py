products = []
while True:
	name = input('請輸入商品名稱: ')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格: ')
	price = int(price)
	#p = [name, price]
	#p = []
	#p.append(name)
	#p.append(price) 這四行可簡化成以下這行
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('product.csv', 'w', encoding='utf-8') as f: #只是打開檔案 encoding='utf-8'(為編碼方式)
	f.write('商品,價格\n') #標題欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #這行才是寫入 ，'\n'是換行符號