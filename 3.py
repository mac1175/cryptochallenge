from collections import Counter
a='1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
#find the highest occurrenc of character of the decoded string
Counter(a.decode('hex'))
#use the character with the highest occurrence to xor each character in decoded string
result=''.join(chr(ord(x) ^ ord('x')) for x in a.decode('hex'))
result.decode('hex')