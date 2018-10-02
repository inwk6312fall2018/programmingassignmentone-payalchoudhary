#Task1

import string

def intname():	
	file = open("running-config.cfg")
	mylist_intname = []	
	""" find the interface and store it in list "mylist_intname" """
	for line in file:
	#remove whitespaces
		line= line.strip(string.punctuation and string.whitespace)
		line= line.split()
		if (line[0] == "interface"):
			mylist_intname.append(line[1])
	return (mylist_intname)

def nameif():	
	file = open("running-config.cfg")	
	mylist_nameif = []
	'''find the nameif and store it in mylist_nameif'''
	for line in file:
	#remove whitespaces
		line= line.strip(string.punctuation and string.whitespace)
		line= line.split()
#		print(line)
		word = line[len(line)-1]
		if(line[0] == "nameif"):
			mylist_nameif.append(line[1])
		if (word == "nameif"):
			mylist_nameif.append("no nameif")
	return (mylist_nameif)	

int_name = intname()
name_if = nameif()
tuple_int_nameif = zip(int_name,name_if)
print(list(tuple_int_nameif))
