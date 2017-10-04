def checkHEX(file):
	# Check if a hex file is in accordance with 'intel HEX' format
	with open(file, 'r') as f:
		lineNo =  1
		EOF = False
		for line in f:
			databytes = int(line[1:3],16)
			datatype = line[7:9]
			checksum = line[9+databytes*2:9+databytes*2+2]

			if EOF:
				print(f.name, ': File format error. Data found after end of file at line', str(lineNo-1))
				return -1
			if datatype == '01':
				EOF = True
			# elif datatype != '00':
			# 	print(f.name, ': Unknown data type found at line %d : %s' %(lineNo, datatype))
			# 	return -1
			if len(line) != 9+databytes*2+2+1:
				print(f.name, ': Data format error at line %d. Number of data bytes does not match with actual data size' %lineNo)
				return -1

			a16 = [line[i:i+2] for i in range(1,9+databytes*2,2)]
			a10 = []
			for a in a16:
				try:
					a10.append(int(a, 16))
				except ValueError:
					print(f.name, ": Invalid literal at line %d. '%s'" %(lineNo, a))
					return -1
			add = sum(a10)%256
			cc10 = ~add+1

			cc16 = hex(cc10 & (2**8-1))
			cc = cc16[2:].upper().zfill(2)
			if checksum != cc:
				print(f.name, ': Checksum error at line', str(lineNo))
				print("Expected :'%s'  Found :'%s'" %(cc, checksum))
				return -1

			lineNo+=1

		return 0

file = 'eeprom_2.eep'
print(checkHEX(file))
