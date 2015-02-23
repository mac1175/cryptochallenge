from collections import Counter
s1= 'Burning \'em, if you ain\'t quick and nimble'

s2='I go crazy when I hear a cymbal'
key='ICE'

def enc(s,size):
    print '=' *50
    print s
    step = size
    
    enc_s=[]
    length =  len(s)
    for i in range(length/step):
        for idx,c in enumerate(s[i*step:(i*step)+step]):
            k= key[idx]
            enc_s.append(chr(ord(c) ^ ord(k)))
    return (''.join(enc_s).encode('hex'))


print enc(s2,3)
print enc(s1,3)
