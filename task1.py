#Task1

file = open("running-config.cfg")
mylist_intname = []
#find the interface
for line in file:
	#remove whitespaces
	line= line.strip()
	#list of string for each line
	line= line.split("!")
	print (line)
	""" check list of 0 is "interface" and copy list of 1"""
	if (line[0] == "interface"):
		mylist_intname.append(line[1])
	
#print(mylist_intname)
