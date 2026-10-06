class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ind_val = {}
        for ind,val in enumerate(nums):
            diff = target - val
            if diff in ind_val:
                return [ind_val[diff], ind]
            ind_val[val] = ind