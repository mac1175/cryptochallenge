from collections import Counter

 
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
    return sum(hamming_bitdiff(ord(c1),ord(c2)) for c1, c2 in zip(s1, s2))
#testing
print hamming_distance('this is a test','wokka wokka!!!')
#37! it works!

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
    return hamming_distance(s1,s2)/key_size

def generate_blocks(key_size,target_string):
    length=len(target_string)
    div_by_ks = length/key_size
    blocks=[]
   
    for b in range(0,key_size-1):

        sb=[]
        blocks[b]=[]
        for i2 in range(0,div_by_ks):
            start2=i2*key_size
            end2=start2+key_size
            curr_string=target_string[start2:end2]
            sb.append(curr_string[b])
            blocks[b].append(''.join(sb))

    for idx,blk in enumerate(blocks):
        print  "%s: %s"%(idx,Counter(blk).most_common(1)[0][0])
    print 'complete'   


key_with_smallest_avg=0
with open("6.txt","r") as f:
    target_string=''.join(f.read().splitlines())
    averages={}
    for ks in range(2,40):
        #print "processing %s"%(ks)
        averages[ks]=find_dist_by_key_size(ks,target_string)
    key_with_smallest_avg=min(averages,key=averages.get)

print "the key is %s"%(key_with_smallest_avg)
generate_blocks(key_with_smallest_avg,target_string)    
