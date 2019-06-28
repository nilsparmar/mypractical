numbers = [1,2,3]
file = open("newfile.txt","w")
for i in numbers:
	file.write(str(i) + "\n")
file.close()


cricketer = {"Name":"Sachin", "Runs":20000, "Century":33}
file = open("newfile2.txt","w")
for i in cricketer:
	file.write(str(i) + " : " + str(cricketer[i]) + "\n")
file.close()


