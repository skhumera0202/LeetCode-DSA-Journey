class Solution(object):
    def myAtoi(self, s):
        INT_MAX= 2147483647
        INT_MIN= -2147483648
        i=0
        n=len(s)
        while i < n and s[i] == ' ':
            i +=1
        sign=1
        if i < n and s[i] == '-':
            sign=-1
            i +=1
        elif i < n and s[i] == '+':
            sign=+1
            i +=1
        limit=INT_MAX if sign==1 else -INT_MIN 
        number=0
        while i < n and s[i].isdigit():
            digit= ord(s[i]) - ord('0')
            if number > limit // 10 or (number == limit // 10 and digit > limit % 10 ):
                return INT_MAX if sign == 1 else INT_MIN
            number=number * 10 + digit
            i += 1
        return sign * number



        """
        :type s: str
        :rtype: int
        """
        