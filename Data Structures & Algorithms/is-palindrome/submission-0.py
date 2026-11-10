class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) <= 1:
            return True
        if not s[0].isalnum():
            return self.isPalindrome(s[1:])
        if not s[-1].isalnum():
            return self.isPalindrome(s[:-1])
        return s[0].lower()==s[-1].lower() and self.isPalindrome(s[1:len(s)-1])