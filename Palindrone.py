class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if list(str(x))==list(str(x))[::-1] else False

print(Solution().isPalindrome("racecar"))
print(Solution().isPalindrome("nigger"))