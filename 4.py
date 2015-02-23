from collections import Counter
arr = []
with open("c:\\4.txt", "r") as ins:
    full_string = ''.join(ins.read().splitlines())

print '=' *50
length = len(full_string)
step = 60
print str(length)+  ' lines'
common = Counter(full_string).most_common(1)[0][0]
print common
for i  in range(length/step):
   a = full_string[i*step:(i*step)+step]
   #print a
   print ''.join(chr(ord(x) ^ ord(Counter(a).most_common(1)[0][0])) for x in a.decode('hex'))
    
