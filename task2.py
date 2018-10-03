import string

def newfile():
	file = open("running-config.cfg",mode = 'r')
	newfile = open("newrunning-config.cfg", mode = 'w')
	
	for line in file:
		line = line.strip(string.punctuation + string.whitespace)
		line = str (line.split())
		line1 = line.replace("172","10")	#replacing 172 with 10
		line2 = line1.replace("192","10")	#replacing 192 with 10
		newfile.write(line2 + "\n")			#writing into new file
	newfile.close()
	file.close()
	#reading from new file
	file1 = open("newrunning-config.cfg",'r')
	for line in file1:
		line = line.strip(string.punctuation + string.whitespace)
		line = line.split()
		print(line)
	newfile.close()

newfile()
