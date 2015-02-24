from collections import Counter
arr = []
with open("4.txt", "r") as ins:
    full_string = ''.join(ins.read().splitlines())

print '=' *50
length = len(full_string)
step = 60
print str(length)+  ' lines'
common = Counter(full_string).most_common(1)[0][0]
print common
for i  in range(length/step):
   start= i*step
   end=start+step
   a = full_string[start:end]
   c=Counter(a).most_common(1)[0][0]
   #print a
   print ''.join(chr(ord(x) ^ ord(c)) for x in a.decode('hex'))
    
