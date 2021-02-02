import os #operating system

def read_file(filename): #### 先讀取檔案
    products = []
    with open(filename, 'r', encoding='utf-8') as f: 
        for line in f:
            if '商品,價格' in line:
                continue #繼續 (跳到下一迴)
            name, price = line.strip().split(',')
            products.append([name, price])
    return products

####讓使用者輸入
def user_input(products):
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
    return products

### 印出購買紀錄
def print_product(products):            
    for p in products:
        print(p[0], '的價格是', p[1])

### 寫入檔案
def write_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f: #只是打開檔案 encoding='utf-8'(為編碼方式)
        f.write('商品,價格\n') #標題欄位
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n') #這行才是寫入 ，'\n'是換行符號

def main():
    filename = 'product.csv'
    if os.path.isfile(filename): #檢查檔案存不存在
        print('找到檔案了!')        
        products = read_file(filename)
    else:
        print('找不到檔案.......')

    product = user_input(products)
    print_product(products)
    write_file('product.csv', products)

main()