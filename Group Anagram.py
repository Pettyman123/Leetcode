def get_counter(s='ava'):
    counter = {}
    for c in s:
        if c in counter:
            counter[c] +=1
        else:
            counter[c] = 1
    return counter

print(get_counter())    
