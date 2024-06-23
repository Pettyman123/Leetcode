jewels = "aA"
stones = "aAbbbb"

def numJewelsInstones(jewels, stones):
    jewels = set(jewels)
    num_jewels = 0
    for s in stones:
        if s in jewels:
            num_jewels += 1
    return num_jewels    
    
print(numJewelsInstones(jewels, stones))