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

