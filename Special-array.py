def isSpecialArray(nums: list[int]) -> bool:
    def parity(x):
        if x % 2 ==1:
            return 'odd'
        else:
            return 'even'
        
    for i in range(1, len(nums)):
        if parity(nums[i]) == parity(nums[i-1]):
            return False
        
    return True


print(isSpecialArray([1,3,4]))
print(isSpecialArray([2,1,4]))