# © Teshan Shanuka J

import datetime, struct, sys

CRC_POLYNOMIAL = 0xEDB88320

EEPROMFILE = 'eeprom.hex'
FLASHFILE = 'flash.hex'

def f2x(f):
	# convert float to hex 
	# http://www.h-schmidt.net/FloatConverter/IEEE754.html
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

WDT_TESTREG = '00'
SP = f2x(37.00)
SPMAX = f2x(38.00)
SPMIN = f2x(36.00)
CF = '00000000'
EN = '00'
HW_VER = f2x(1.00)
FW_VER = f2x(1.00)

now = datetime.datetime.now()
y = now.year; m = now.month; d = now.day

#######################################

# def findLineBeforeLast(eepfile):
# 	with open(eepfile, 'r') as f:
# 		isEvenLineNo = False
# 		line0 = line1 = ''

# 		line = line0 = f.readline()
# 		while True:
# 			line = f.readline()
# 			if line == '':
# 				break
# 			if isEvenLineNo:
# 				line0 = [line[:-3],f.tell()]
# 			else:
# 				line1 = [line[:-3],f.tell()]
# 			isEvenLineNo = not isEvenLineNo

# 		if isEvenLineNo:
# 			lineInfo = line0
# 		else:
# 			lineInfo = line1

# 	return lineInfo

def findLineBeforeLast(eepfile):
	# returns line num
	with open(eepfile, 'r') as f:
		isEvenLineNo = False
		linePos0 = linePos1 = 0

		line = f.readline()
		while True:
			line = f.readline()
			if line == '':
				break
			if isEvenLineNo:
				linePos0 = f.tell()
			else:
				linePos1 = f.tell()
			isEvenLineNo = not isEvenLineNo

		if isEvenLineNo:
			pos = linePos0
		else:
			pos = linePos1

	return pos

# def createCRCline(line,EEPROMCRC,FlashCRC):
# 	# Create string including CRCs to replace line prior to last line 
# 	# Returns data string without cc bytes
# 	databytes = int(line[1:3],16)
# 	if len(line) != 9+databytes*2:
# 		print('createCRCline: Data format error. Number of data bytes does not match with actual data bytes')
# 		input("Press Enter to continue...")
# 		exit()
# 	CRCline = line[:9+databytes*2-16]+EEPROMCRC+FlashCRC
# 	return CRCline

def addLineChecksum(line):
	# Takes hex data string without cc bytes
	# Returns complete data line with added cc
	databytes = int(line[1:3],16)
	a16 = [line[i:i+2] for i in range(1,9+databytes*2,2)]
	a10 = []
	for a in a16:
		a10.append(int(a, 16))
	# The checksum is calculated by summing the values of all hexadecimal digit pairs 
	# in the record modulo 256 and taking the two's complement. 
	# http://www.keil.com/support/docs/1584/
	add = sum(a10)%256
	cc10 = ~add+1

	cc16 = hex(cc10 & (2**8-1))
	cc = cc16[2:].upper().zfill(2)
	lineWithChecksum = line+cc+'\n'
	return lineWithChecksum

# def writeHEX(eepfile, info, CRCline, CRClineLocation, newHEXfile):
# 	newHEX = open(newHEXfile, 'w')
# 	infoWritten = False
# 	with open(eepfile, 'r') as f:
# 		# Write device information and initial values to EEPROM
# 		i = 0
# 		while (i < len(info) and not infoWritten):
# 			line = f.readline()
# 			databytes = int(line[1:3],16)

# 			if len(line) != 11+databytes*2+1:
# 				print('writeHEX: Data format error. Number of data bytes does not match with actual data bytes')
# 				input("Press Enter to continue...")
# 				f.close()
# 				exit()

# 			if(databytes*2 <= len(info) - i):
# 				newline = line[:9] + info[i:i+databytes*2]
# 				i+=databytes*2
# 			else:
# 				newline = line[:9] + info[i:] + line[9+len(info)-i:9+databytes*2]
# 				infoWritten = True

# 			fullLine = addLineChecksum(newline[:9+databytes*2])
# 			newHEX.write(fullLine)

# 		# Write EEPROM and Flash CRCs to the end of the file
# 		line = f.readline()
# 		while  True:
# 			if line == '':
# 				break
# 			linePos = f.tell()
# 			if(linePos == CRClineLocation):
# 				databytes = int(line[1:3],16)
# 				newHEX.write(line[:9+databytes*2-16])
# 				newHEX.close()
# 			else:
# 				newHEX.write(line)

# 			line = f.readline()

def writeHEX(eepfile, FlashCRC, neweepfile, info, CRClinePos):
	newHEX = open(neweepfile, 'w')
	newHEXopened = True
	infoWritten = False
	with open(eepfile, 'r') as f:
		# Write device information and initial values to EEPROM
		i = 0
		while (i < len(info) and not infoWritten):
			line = f.readline()
			databytes = int(line[1:3],16)

			if(databytes*2 <= len(info) - i):
				newline = line[:9] + info[i:i+databytes*2]
				i+=databytes*2
			else:
				newline = line[:9] + info[i:] + line[9+len(info)-i:9+databytes*2]
				infoWritten = True

			fullLine = addLineChecksum(newline[:9+databytes*2])
			newHEX.write(fullLine)

		# Write rest of the hex file untill find the location to put file CRCs
		line = f.readline()
		while  True:
			if line == '':
				break
			linePos = f.tell()
			if(linePos == CRClinePos):
				databytes = int(line[1:3],16)
				newHEX.write(line[:9+databytes*2-16])
				newHEX.close()
				newHEXopened = False
				break
			else:
				newHEX.write(line)

			line = f.readline()

		# Write CRCs to file
		EEPROMCRC = hex(calcFileCRC(neweepfile))
		EEPROMCRC = EEPROMCRC[2:].upper()

		if newHEXopened:
			print('EEPROM file write failed. \nNew HEX file is not written properly. Check the code and the EEPROM file...')
			return
		newf = open(neweepfile, 'a+')
		newf.seek(0)
		for l in newf:
			pass
		newHEXline = l + EEPROMCRC + FlashCRC
		newHEXline = addLineChecksum(newHEXline)

		newf.write(newHEXline[len(l):])

		line = f.readline()
		newf.write(line)

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

def checkHEX(file):
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
				a10.append(int(a, 16))
			add = sum(a10)%256
			cc10 = ~add+1

			cc16 = hex(cc10 & (2**8-1))
			cc = cc16[2:].upper().zfill(2)
			if checksum != cc:
				print(f.name, ': Checksum error at line', str(lineNo))
				return -1

			lineNo+=1

		return 0

# def calcFlashCRC(flashfile,lineBeforeLast):
# 	crc = 0
# 	with open(flashfile, 'r') as f:
# 		line = f.readline()
# 		repr(line)
# 		while  True:
# 			databytes = int(line[1:3],16)
# 			if len(line) != 11+databytes*2+1:
# 				print('calcFlashCRC: Data format error. Number of data bytes does not match with actual data bytes')
# 				return -1
# 			if line == '':
# 				print('Something wrong with the file...')
# 				return -1

# 			linePos = f.tell()
# 			if(linePos == lineBeforeLast):
# 				hexdat = [line[i:i+2] for i in range(1,len(line)-1-18,2)]
# 				for dat in hexdat:
# 					crc = CRC32oneByte(int(dat,16), crc)
# 				for i in range(4):
# 					crc = CRC32oneByte(0, crc)
# 				return crc
# 			else:
# 				hexdat = [line[i:i+2] for i in range(1,len(line)-1,2)]
# 				for dat in hexdat:
# 					crc = CRC32oneByte(int(dat,16), crc)

# 			line = f.readline()
# 	return -1

def calcFileCRC(file):
	crc = 0
	with open(file, 'r') as f:
		for line in f:
			hexdat = [line[i:i+2] for i in range(1,len(line)-1,2)]
			for dat in hexdat:
				crc = CRC32oneByte(int(dat,16), crc)
			for i in range(4):
				crc = CRC32oneByte(0,crc)
	return crc

#########################################

if __name__ == '__main__':
	# Check eeprom and flash hex files for any errors
	if(checkHEX(EEPROMFILE) != 0 or checkHEX(FLASHFILE) != 0):
		sys.exit()

	# Get date confirmation
	print('Date :', now.date())
	input('If this date is not correct please restart this program after setting your system date correctly!\n' \
		'press Enter to continue...')

	# Get number of units to produce
	while True:
		try:
			noOfUnits = int(input('\nEnter the number of units : '))
			break
		except ValueError:
			print('Input data type error. Please enter an integer')

	CRClinePos = findLineBeforeLast(EEPROMFILE)

	FlashCRC = hex(calcFileCRC(FLASHFILE))
	FlashCRC = FlashCRC[2:].upper()

	for unit_no in range(1,noOfUnits+1):
		sn = str(y)+str(m).zfill(2)+str(d).zfill(2)+str(unit_no).zfill(4)
		
		SERIAL_NUMBER = ''.join(['0'+sn[i] for i in range(len(sn))])
		newEEPROMfileName = 'eeprom_'+str(unit_no)+'.hex'

		info = WDT_TESTREG+ \
				SP[2:].upper()+ \
				SPMAX[2:].upper()+ \
				SPMIN[2:].upper()+ \
				CF+ \
				EN+ \
				SP[2:].upper()+ \
				SPMAX[2:].upper()+ \
				SPMIN[2:].upper()+ \
				CF+ \
				EN+ \
				SERIAL_NUMBER+ \
				HW_VER[2:].upper()+ \
				FW_VER[2:].upper()

		writeHEX(EEPROMFILE, FlashCRC, newEEPROMfileName, info, CRClinePos)

		if(checkHEX(newEEPROMfileName) != 0):
			print('Something went wrong with writing the HEX file')
			sys.exit()









# newHEXfile = 'eeprom_1.hex'

# lineInfoToReplace = findLineBeforeLast(EEPROMfile)

# EEPROMCRC = hex(calcFileCRC(EEPROMfile))
# EEPROMCRC = EEPROMCRC[2:].upper()

# FlashCRC = hex(calcFlashCRC(Flashfile, lineInfoToReplace[1]))
# FlashCRC = FlashCRC[2:].upper()

# lineWithCRCs = createCRCline(lineInfoToReplace[0],EEPROMCRC,FlashCRC)
# fullLine = addLineChecksum(lineWithCRCs)

# writeNewHEX(EEPROMfile, lineInfoToReplace, fullLine)

input("Press Enter to continue...")
