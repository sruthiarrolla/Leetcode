class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def generate(ind,curr_subset,ans,candidates,target):
            if(target==0):
                ans.append(curr_subset.copy())
                return
            if(target<0):
                return
            if(ind==len(candidates)):
                return
            curr_subset.append(candidates[ind])
            generate(ind+1,curr_subset,ans,candidates,target-candidates[ind])
            curr_subset.pop()
            for i in range(ind+1,len(candidates)):
                if(candidates[ind]!=candidates[i]):
                    ind=i
                    generate(ind,curr_subset,ans,candidates,target)
                    break
        ind=0
        ans=[]
        curr_subset=[]
        candidates.sort()
        generate(ind,curr_subset,ans,candidates,target)
        return ans
        