class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False 
        orignal=x
        reverse=0
        while x > 0:
            digit=x % 10
            reverse=reverse * 10 +digit
            x=x // 10
        return orignal==reverse 
        """
        :type x: int
        :rtype: bool
        """
        