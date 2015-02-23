a="1c0111001f010100061a024b53535009181c"
b="686974207468652062756c6c277320657965"
''.join(chr(ord(x) ^ ord(y)) for x,y in zip(a.decode('hex'),b.decode('hex'))).encode('hex')