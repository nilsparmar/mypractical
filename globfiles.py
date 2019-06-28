import glob2
from datetime import datetime

filenames = glob2.glob("file*.txt")

with open(datetime.now().strftime("%d-%m-%Y-%H-%M-%S-%f")+".txt",'w') as fw:
	for filename in filenames:
		with open(filename,'r') as fr:
			fw.write(fr.read()+"\n")
