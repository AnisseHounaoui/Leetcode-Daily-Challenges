#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.
#Example 1:
#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

class October09(object):
    def runningSum(self, nums):
        sum = []
        
        for i in range(len(nums)):
            calc = 0
            for j in range(i+1):
                calc += nums[j]
            sum.append(calc)
        return sum
