data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # %是用來求餘數；若count/1000的餘數為0
			print(len(data))
print('已讀取完檔案，共有', len(data), '筆資料')
print('---')
sum_len = 0
for d in data:
	sum_len += len(d) # sum_len = sum_len + len(d)
print('留言總長度為', sum_len)
print('---')
print('留言的平均長度為', sum_len/len(data))


# 篩選
new = []
for d in data: # for loop的意思就是「把清單中的東西一個一個拿出來」d是字串data是清單
	if len(d) < 100:
		new.append(d)
print('共有', len(new), '筆留言長度小於100')
print(new[0])

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('共有', len(good), '筆留言提到good')
print(good[0])

# list comprehension(清單快寫法) 35行等於27~30行
good = [d for d in data if 'good' in d]
# 第一個d = good.append(d)的d
print(len(good))

bad = ['bad' in d for d in data] # 'bad' in d 運算（true/false)
print(bad)
# output = [(number-1) for number in reference if number % 2 == 0]
#              運算          變數        清單           篩選條件


# 文字計數
wc = {} # word_count
for d in data:
	words = d.split()
	for word in words:
		if word in wc:
			wc[word] += 1
		else:
			wc[word] = 1 # 新增新的key進wc字典

for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Ben'])

while True:
	word = input('輸入你想查的字：')
	if word == 'q':
		break
	if word in wc:
		print(word, '出現過：', wc[word], '次')
	else:
		print('這個字沒出現過！')

print('程式結束')




