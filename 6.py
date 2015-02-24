from collections import Counter
from operator import itemgetter
 
def hamming_bitdiff(c1, c2):
    """Return the Hamming distance between equal-length sequences"""
    dist=0
    val= c1 ^ c2
    while(val !=0):
        dist+=1
        val &=val-1
    return dist

def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(hamming_bitdiff(ord(c1),ord(c2)) for c1, c2 in zip(s1, s2))/float(len(s1))
#testing
print hamming_distance('this is a test','wokka wokka!!!')
#37! it works!

def single_byte_xor(b,s):
     return ''.join(chr(ord(x) ^ b) for x in s.decode('hex'))

def find_dist_by_key_size(key_size,target_string):
    distances =[]
    length=len(target_string)
    div_by_ks = length/key_size
    for i in range(0,div_by_ks-1):
        start1=i*key_size
        end1=start1+key_size
        start2=(i+1)*key_size
        end2=start2+key_size
        #print "[%s,%s] vs [%s,%s]"%(start1,end1,start2,end2)
        s1=target_string[start1:end1]
        s2=target_string[start2:end2]
        #"%s compared to %s"%(s1,s2)
    return hamming_distance(s1,s2)

def transpose_blocks(key_size,target_string):
    length=len(target_string)
    div_by_ks = length/key_size
    blocks=[]
   
    for b in range(0,key_size):
        blocks.append([])
        for i2 in range(0,div_by_ks):
            start2=i2*key_size
            end2=start2+key_size
            curr_string=target_string[start2:end2]
            blocks[b].append(curr_string[b])
    return blocks

def decrypt_string(key,target_string):
    distances =[]
    length=len(target_string)
    key_size=len(key)
    div_by_ks = length/key_size

    #print 'key_size: %s'%(key_size)
    #print 'div_by_ks: %s'%(div_by_ks)
    result=[]
    #print "ky is '%s'"%(key)
    for i in range(0,div_by_ks):
        start=i*key_size
        end=start+key_size
        print ''.join(chr(ord(k) ^ ord(c)) for k,c in  zip(key,target_string[start:end]))




with open("6.txt","r") as f:
    target_string=''.join(f.read().splitlines()).decode('base64').encode('hex')
    #print target_string
    distances={}
    for ks in range(2,40):
        #print "processing %s"%(ks)
        distances[ks]=find_dist_by_key_size(ks,target_string)

print distances

blocks=transpose_blocks(29,target_string)

for blk in blocks:
    for i in range(0,256):
        print single_byte_xor(i,''.join(blk))

