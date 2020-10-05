import string
import time

plaintext = "fvbdpssulclyulclyjyhjraopzjvklpmfvbkvaolufvbtbzailzvtlrpukvmnlupbz"

def caesar(plaintext, key):
	ciphertext = ""
	for letter in plaintext:
		location = ord(letter) + key
		if letter in string.punctuation:
			ciphertext += letter
		else:
			if letter.lower() != letter:
				if location < 65:
					location += 26
				elif location > 90:
					location -= 26
			else:
				if location < 97:
					location += 26
				elif location > 122:
					location -= 26
			
			ciphertext += chr(location)
	
	return(ciphertext)

def freqAnalysis(plaintext):
	frequency = []
	for i in range(97, 97+26):
		frequency.append({"char": chr(i), "count": plaintext.count(chr(i))})
	
	a= time.time()
	sorted_l = sorted(frequency, key= lambda x: x["count"])
	key1 = ord("e") - ord(sorted_l[len(sorted_l) - 1]["char"])
	b = time.time()
	key2 = ord("e") - ord(max(frequency, key= lambda x: x["count"])["char"])
	c = time.time()
	time1 = b-a
	time2 = c-b
	return(time1, time2)
	#print(caesar(plaintext, key))

freqAnalysis(plaintext)

n= 1000000
times = []
for i in range(n):
	times.append(freqAnalysis(plaintext))

print(sum(times[1])/n)
print(sum(times[0])/n)

'''
for key in range(26):
	print(caesar(plaintext, key))
'''
