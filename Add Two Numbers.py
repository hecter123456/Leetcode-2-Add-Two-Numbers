import unittest
import itertools
class unitest(unittest.TestCase):
    def testOverflow(self):
        l1 = [2,4,3]
        l2 = [5,6,4]
        ans = [7,0,8]
        self.assertEqual(Solution().addTwoNumbers(l1,l2),ans)
    def testDiffDigits(self):
        l1 = [2,4,3,5]
        l2 = [5,6,4]
        ans = [7,0,8,5]
        self.assertEqual(Solution().addTwoNumbers(l1,l2),ans)

class Solution():
    def addTwoNumbers(self, l1, l2):
        def fn(a,b):
            if a is None and b is None:
                return 0
            if a is None:
                return b
            if b is None:
                return a
            return a + b
        ans = []
        overflow = 0
        for a,b in itertools.zip_longest(l1,l2):
            c = fn(a,b)
            ans.append(int(c)%10+overflow)
            overflow = int((c)/10)
        return ans

if __name__ == '__main__':
    unittest.main()
