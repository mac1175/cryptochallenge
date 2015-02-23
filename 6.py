
 
def hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(b1 != b2 for b1, b2 in zip(s1,s2))

print hamming_distance('this is a test','wokka wokka!!!')
