a = 1
b = "2"

print(int(3.6))
try:
	print(a+b)

# except TypeError:
# 	print("This is TypeError")

# except:
# 	print("Just Error(not defined which error...")

except TypeError as ae:
	print("Error is:",ae)


