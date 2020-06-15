import unittest

class Solution:
    def twoSum(self, nums, target):
        dict1 = {}

        for i, num in enumerate(nums):
            if (target - num) in dict1:
                return [i, dict1[target - num]]
            else:
                dict1[num] = i


class TestDict(unittest.TestCase):

    def test(self):
        solu = Solution()
        self.assertEqual(sorted(solu.twoSum([2, 7, 11, 15],9)),[0,1])
        self.assertEqual(sorted(solu.twoSum([2, 7, 11, 15],13)),[0,2])


if __name__ == '__main__':
    unittest.main()