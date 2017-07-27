import unittest
import NodeSolution

class unitest(unittest.TestCase):
    def testOverflow(self):
        row = [2,4,3]
        l1 = NodeSolution.NodeSolution().AddNode(row)
        row = [5,6,4]
        l2 = NodeSolution.NodeSolution().AddNode(row)
        ans = [7,0,8] 
        self.assertEqual(Solution().addTwoNumbers(l1,l2),ans)
    def testDiffDigits(self):
        row = [2,4,3,5]
        l1 = NodeSolution.NodeSolution().AddNode(row)
        row = [5,6,4]
        l2 = NodeSolution.NodeSolution().AddNode(row)
        ans = [7,0,8,5]
        self.assertEqual(Solution().addTwoNumbers(l1,l2),ans)

class Solution():
    def addTwoNumbers(self, l1, l2):
        ans = []
        overflow = 0
        while l1 or l2 or overflow:
            if l1:
                overflow += l1.val 
                l1 = l1.next
            if l2:
                overflow += l2.val
                l2 = l2.next
            overflow, val = divmod(overflow,10)
            ans.append(val)
        return ans

if __name__ == '__main__':
    unittest.main()
