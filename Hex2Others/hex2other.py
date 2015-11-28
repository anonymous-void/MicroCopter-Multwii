import re
def hex2dec (hexString):
	hexDict = {'A':10, 'a':10, 'B':11, 'b':11, 'C':12, 'c':12, 'D':13, 'd':13, 'E':14, 'e':14, 'F':15, 'f':15, '1':1, \
	'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '0':0}
	number2return = 0
	for items in hexString:
		if (items == '\t') or (items == '\n') or (items == '') or (items == '\r'):
			return hexString
		else:
			number2return = number2return * 16 + hexDict[items]
	return str(number2return)

suffix = "_DEC"
fileFromName = "eepromReadResult-BeforeWrite.txt"
fileToName = "eepromReadResult-BeforeWrite" + suffix + ".txt"

fileFromPointer = open(fileFromName, "r")
fileObjFrom = fileFromPointer.readlines()

fileToPointer = open(fileToName, "w")

for lines in fileObjFrom:
	thisLine = lines.split('\t')
	for stringAtom in thisLine:
		reJudger = re.match(r'^EEPROM', stringAtom)
		if reJudger:
			print stringAtom
			fileToPointer.write(stringAtom)
			continue
		if stringAtom != "\r\n":
			print hex2dec(stringAtom),
			fileToPointer.write(hex2dec(stringAtom) + '\t')
		else:
			fileToPointer.write(hex2dec(stringAtom))
	print thisLine
fileFromPointer.close()
fileToPointer.close()