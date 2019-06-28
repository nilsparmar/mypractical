file = open('fruits.txt')
data = file.read()
file.close()
print(data)

with open('fruits.txt',"r") as f:
	