temperature = [10, -20, -289, 100]


def writer(temperature, filepath):
	with open(filepath, 'w') as file:
		for c in temperature:
			if c > -273.15:
				f = c* 9/5 + 32
				file.write(str(f) + "\n")

writer(temperature, "temps.txt")