CRC_POLYNOMIAL = 0xEDB88320
################ CRC ###################

def CRC32oneByte(nextByte, CRC):
	for i in range(8):
		if (CRC & 0x80000000):
			CRC = CRC << 1
			# check whether the next byte has one or zero which is going to be shifted to CRC
			if (nextByte & 0x80):
				 # set last bit of the value 
				CRC |= 0x01
			else:
				CRC &= 0xFFFFFFFE
			CRC ^= CRC_POLYNOMIAL
		else:
			CRC = CRC << 1
			# check whether the next byte has one or zero which is going to be shifted to CRC
			if (nextByte & 0x80):
				 # set last bit of the value 
				CRC |= 0x01
			else:
				CRC &= 0xFFFFFFFE
		nextByte = nextByte << 1
	return CRC

def calcFileCRC(file):
	crc = 0
	with open(file, 'r') as f:
		for line in f:
			databytes = int(line[1:3],16)
			datatype = line[7:9]
			if datatype == '01':
				break
			hexdat = [line[i:i+2] for i in range(9,min(9+databytes*2,len(line)-1),2)]
			print(hexdat)
			for dat in hexdat:
				crc = CRC32oneByte(int(dat,16), crc)
		for i in range(4):
			crc = CRC32oneByte(0,crc)
	return crc

file = 'correctOne.eep'
print(hex(calcFileCRC(file)))
