s = "egg"
t = "add"






def isIsomorphic( s: str, t: str) -> bool:
    if len(s) == len(t):
        for i in range(len(s)):
            if s[i] != t[i]:
                return True
            else:
                return False
            
print(isIsomorphic(s ,t ))

copiht = {}
for char in s:
    copiht[char] = 0

print(copiht)