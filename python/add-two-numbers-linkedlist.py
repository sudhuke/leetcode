#class ListNode:

 #   def __init__(self, val):
  #      self.val = val
   #     self.next = None

    #def __init__(self):
     #   self.next = None


class Solution:
    
    def __init__(self):
        self.head = None
        self.size = 0
        self.sum = ' '

    def insertNode(self, val):
        node = ListNode(val)
        node.next = self.head
        self.head = node
        return True

    def printNode(self, node):
        ans = "["
        curr = node
        print(curr.next)
        while curr:
            ans += str(curr.val)
            # print(ans)
            if curr.next:
                ans += ","
            curr = curr.next
        print(ans)
        return node

    def add_nodes(self, node):
        curr = node
        while curr:
            self.sum += str(curr.val)
            curr = curr.next
        return str(self.sum)[::-1]
        # return str(self.sum)[::-1]

    def insertNodes(self, final_str):
        for eachStr in list(final_str):
            node = ListNode(eachStr)
            node.next = self.head
            self.head = node
        return node

    def addTwoNumbers(self, input_list1, input_list2)->ListNode:
        #list1 = LinkedList()
        ans1 = Solution().add_nodes(input_list1)
        ans2 = Solution().add_nodes(input_list2)
        final = str(int(ans1) + int(ans2))
        print(final)
        node = ListNode(0)
        node = Solution().insertNodes(final)
        # final_list.printNode(node)
        return node


