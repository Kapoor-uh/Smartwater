def ParseHighQualityPumps():
	pumps = []
	with open('flowquality.csv') as f:
		lines = f.readlines()
	for line in lines[1:]:
		split = line.split(',')
		if(split[0].startswith('JVP') and split[2] == '1'):
			pumps.append(split[0])
	return pumps
