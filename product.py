#### 先讀取檔案
products = []
with open('product.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue #繼續 (跳到下一迴)
		name, price = line.strip().split(',') #先用strip 把換行符號'\n'去掉，在用split() 切割成"清單"
		products.append([name, price])
print(products)

####讓使用者輸入
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

### 印出購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

### 寫入檔案
with open('product.csv', 'w', encoding='utf-8') as f: #只是打開檔案 encoding='utf-8'(為編碼方式)
	f.write('商品,價格\n') #標題欄位
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n') #這行才是寫入 ，'\n'是換行符號