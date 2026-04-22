class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n=len(s)
        m=len(t)
        d={}
        for ch in t:
            if(ch in d):
                d[ch]+=1
            else:
                d[ch]=1
        left,right=0,0
        minLen=float("inf")
        count=0
        sIndex=-1
        while(right<n):
            if(s[right]in d and d[s[right]]>0):
                count+=1
            if(s[right]in d):
                d[s[right]]-=1
            else:
                d[s[right]]=-1
            while(count==len(t)):
                if((right-left+1)<minLen):
                    minLen=right-left+1
                    sIndex=left
                d[s[left]]+=1
                if(d[s[left]]>0):
                    count-=1
                left+=1
            right+=1
        if(sIndex==-1):
            return ""
        return(s[sIndex:sIndex+minLen])
        