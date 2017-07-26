import unittest

class unitest(unittest.TestCase):
    def testOverflow(self):
        l1 = [2,4,3]
        l2 = [5,6,4]
        ans = [7,0,8]
        self.assertEqual(Solution().addTwoNumbers(l1,l2),ans)

class Solution():
    def addTwoNumbers(self, l1, l2):
        ans = []
        overflow = 0
        for a,b in zip(l1,l2):
            ans.append((a+b)%10+overflow)
            overflow = int((a+b)/10)
        return ans

if __name__ == '__main__':
    unittest.main()
