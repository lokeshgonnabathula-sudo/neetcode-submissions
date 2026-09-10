class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for i,n in enumerate(nums):
            n1=target-n
            if n1 in hm:
                return [hm[n1],i]
            hm[n]=i