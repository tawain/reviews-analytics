data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # %是用來求餘數；若count/1000的餘數為0
			print(len(data))
print(len(data))

print(data) # ctrl + c 強制中斷程式
print('---')
print(data[0])
print('---')
print(data[1])