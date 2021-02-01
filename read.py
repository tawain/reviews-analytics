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

