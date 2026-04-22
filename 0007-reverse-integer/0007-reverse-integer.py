class Solution:
    def reverse(self, x: int) -> int:
        original=x
        if(x<0):
            x=-1*x
        rev=0
        while(x>0):
            rem=x%10
            rev=(rev*10)+rem
            x=x//10
        if(rev<(-2**31)) or rev>((2**31)-1):
            return 0
        if(original<0):
            return -rev
        else:
            return rev
        