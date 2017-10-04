# © Teshan Shanuka J


dec_table = {'A':0,  'B':1,  'C':2,  'D':3,  'E':4,  'F':5,  'G':6,  'H':7,  \
			 'I':8,  'J':9,  'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, \
			 'Q':16, 'R':17, 'S':18, 'T':19, 'U':20, 'V':21, 'W':22, 'X':23, \
			 'Y':24, 'Z':25, 'a':26, 'b':27, 'c':28, 'd':29, 'e':30, 'f':31, \
			 'g':32, 'h':33, 'i':34, 'j':35, 'k':36, 'l':37, 'm':38, 'n':39, \
			 'o':40, 'p':41, 'q':42, 'r':43, 's':44, 't':45, 'u':46, 'v':47, \
			 'w':48, 'x':49, 'y':50, 'z':51, '0':52, '1':53, '2':54, '3':55, \
			 '4':56, '5':57, '6':58, '7':59, '8':60, '9':61, '+':62, '/':63}

glass_types =  {'11111111':'GLASS TYPE ERROR', \
				'00000001':'ICSI', \
				'00000010':'WORKSTATION', \
				'00000011':'TABLE', \
				'00000100':'TABLETOP'}

system_status =    ['NO_ERROR', \
					'INA2_FAULT', \
					'INA1_FAULT', \
					'VDRIVE_FAULT', \
					'WDT_CHECK_FAULT', \
					'RTC_FAULT', \
					'WDT_RESET', \
					'BUZZER_FAULT', \
					'DISPLAY_CONTENT_FAULT', \
					'EEPROM_CRC_FAULT', \
					'POWER_FAULT']

glass_status = ['GLASS_DETECTION_ERROR', \
				'GLASS_DISCONNECT', \
				'OVER_TEMPERATURE', \
				'UNDER_TEMPERATURE', \
				'SENSOR_ERROR', \
				'RATE_OF_HEAT_ERROR', \
				'AT_ERROR', \
				'AC_ERROR', \
				'TERMINAL_BREAK_ERROR', \
				'SHORT_CIRCUIT_GLASS', \
				'GLASS_STATUS_OK', \
				'GLASS_DISABLE', \
				'GLASS_IS_AUTO_TUNNING', \
				'GLASS_IS_CALIBRATING']

def x64toErrMsg(message):
	if(len(message) is not 19):
		print("Message size does not match HGS1000 error message format...")
		return
	decVal = [dec_table[l] for l in message]
	binVal = [bin(v)[2:].zfill(6) for v in decVal]
	# Reverse the array
	# binVal = binVal[::-1]
	binArr = ''.join(binVal)

	errArr = [binArr[2:8+2], binArr[10:10+8], binArr[18:18+32], binArr[50:50+32], binArr[82:]]
	# errArr = [binArr[:32], binArr[32:32+32], binArr[64:64+32], binArr[96:96+8], binArr[104:]]
	return errArr

message = input('Enter error code:\t')
while len(message) is not 19:
	message = input('Error code must be of length 19. Try again:\t')
# message = 'HOpSWQwm2lKcVlJTrVf'

ERR_DISCRIPTION = [ 'channel2GlassType', 'channel1GlassType', 'systemStatus', 'channel2GlassStatus', 'channel1GlassStatus']
ERR = x64toErrMsg(message)
try:
	print()
	print('CH 1 Glass Type : ', glass_types[ERR[1]])
	if ERR[1] != '11111111':
		print('Glass Status :')
		for i in range(len(glass_status)):
			if ERR[4][-1-i] == '1':
				print('\t', glass_status[i])
except KeyError:
	print('Unidentified glass type in CH 1')

try:
	print()
	print('CH 2 Glass Type : ', glass_types[ERR[0]])
	if ERR[0] != '11111111':
		print('Glass Status :')
		for i in range(len(glass_status)):
			if ERR[3][-1-i] == '1':
				print('\t', glass_status[i])
except KeyError:
	print('Unidentified glass type in CH 2')

print()
print('System Errors :')
for i in range(len(system_status)):
	if ERR[2][-1-i] == '1':
		print('\t',system_status[i])

print()
for i in range(5):
	print(ERR_DISCRIPTION[i], ' : ', ERR[i])

input('press enter to continue...')
