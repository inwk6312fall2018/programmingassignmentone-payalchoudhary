#Task1
import string

file = open("running-config.cfg")
mylist_intname = []
mylist_nameif = []
""" find the interface and store it in list "mylist_intname" """
for line in file:
	#remove whitespaces
	line= line.strip(string.punctuation and string.whitespace)
	#list of string for each line
	line= line.split()
#	print (line)
	""" check if list of 0 is "interface" and copy list of 1"""
	if (line[0] == "interface"):
		mylist_intname.append(line[1])
	""" check if list of 0 is "nameif" and copy list of 1"""
	if (line[0] == "nameif"):
		mylist_nameif.append(line[1])	
#print(mylist_intname)
print(mylist_nameif)
