class Solution:
    def isPalindrome(self, s: str) -> bool:
        # setup left/right points that goes into middle, compare s[l] and s[r], return false if not the same
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
            if not s[r].isalnum():
                r -= 1
            # check if char if alpha
            if s[l].isalnum() and s[r].isalnum():
                if s[l].lower() != s[r].lower():
                    return False
                else:
                    l += 1
                    r -= 1

        # return true if pointers meet at middle. 
        return True