'''
Author: Arthur Lacey
16FEB16
Parses a bit string to decode it into it's character string equivalent
e.g.
>>> a='010000010100001101000100'
>>> parseBitString(a,0)
'ACD'
'''
from multiprocessing import *

bitsInAByte=8 #this is a constant value

def parseBitString(string, startIndex):
    message="" #stores the decoded message
    
    i=startIndex #i represents the beginning of the substring to examine
    while(i<len(string)):#if i is greater, there will be no substring
        substring=string[i:i+bitsInAByte]
        if(len(substring)==8): #if the length is not 8, it's not safe to look for a letter
            message=message+chr(int(substring,2)) #http://stackoverflow.com/questions/8928240/convert-binary-string-to-int
        i+=bitsInAByte
    return message
            
def parseAllStrings(string):
	pool=Pool(processes=bitsInAByte)
	messages= [None]*bitsInAByte

	
	for i in range(bitsInAByte):
		messages[i]=pool.apply_async(parseBitString,[string,i])

	for i in range(len(messages)):
		messages[i]=messages[i].get()
	
	#pool.map(parseBitString,string,range(bitsInAByte))
	
	#return pool
	return messages

def generateBitString(string): #used for testing purposes
	output=""
	for letter in string:
		binaryString=bin(ord(letter))[2:]
		while(len(binaryString)<8):
			binaryString="0"+binaryString
		output=output+binaryString
	return output



