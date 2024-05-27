strs = ["'eat', 'tea', 'tan', 'ate', 'nat', 'bat'"]

#output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]

def groupAnagrams(strs: list[str]): 
    ans = {}
    for s in strs:
        S_sroted = sorted(s)
        key = tuple(S_sroted)

        if key not in ans:
            ans[key] = [s]
        else:
            ans[key].append(s)
    return ans.values()


print(groupAnagrams(strs))