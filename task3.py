import string

def accesslist():
	file = open("running-config.cfg")
	
	for line in file:
		line = line.strip(string.punctuation + string.whitespace)
		line = line.split()
		for item in line:
			if (line[0] == "access-list"):
				if (line[1] == "global_access" or line[1] == "fw-management_access_in"):
					print(list(line))
	file.close()

accesslist()
