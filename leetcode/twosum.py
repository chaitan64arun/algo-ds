class Solution(object):
    def twoSum(self, nums, target):
        itr = len(nums)
        d = {}
        for i in xrange(itr):
            if ((target - nums[i]) in d.iterkeys()):
                return [d[target - nums[i]], i]
            else:
                d[nums[i]] = i



''' Naive half solution

    def twoSum(self, nums, target):
        itr = len(nums)

        for i in xrange(itr):
            for j in xrange(i):
                if (target == nums[i] + nums[j]):
                    return [j,i]
'''
''' Naive solution
    def twoSum(self, nums, target):
        itr = len(nums)

        for i in xrange(itr):
            for j in xrange(itr):
                if (target == nums[i] + nums[itr-j-1]):
                    return [i,j-1]
'''
