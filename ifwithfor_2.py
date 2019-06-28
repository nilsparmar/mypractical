# mylist = [1,2,3,4,5]

# for i in mylist:
# 	if i > 2:
# 		print(i)


with open("fruits.txt") as f:
	data = f.read()
	data = data.splitlines()

for i in data:
	print(len(i))