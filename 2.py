# Add two numbers
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        el1 = []
        while True:
            if l1 == None:
                print(el1)
                break
            else:
                el1.append(l1.val)
                l1 = l1.next

        el2 = []
        while True:
            if l2 == None:
                break
            else:
                el2.append(l2.val)
                l2 = l2.next
        print(el1, el2)
        res_list = []
        for i in range(0, len(el1)):
            res_list.append(el1[i] + el2[i])
        print(res_list)
        for i in range(len(res_list)):
            if res_list[i] > 9:
                res_list[i] = (res_list[i])%10
                if (i+1) == len(res_list):
                    res_list.append(1)
                else:
                    res_list[i+1] = res_list[i+1] + 1
        print(res_list)


    # Solution given:
    # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummyHead = ListNode(0)

        p = l1
        q = l2
        curr = dummyHead
        carry = 0
        while (p != None or q != None):
            if (p != None):
                x = p.val
            else:
                x = 0
            if (q != None):
                y = q.val
            else:
                y = 0
            #print(type(carry), type(x), type(y))
            sum = carry + x + y;
            carry = sum / 10
            carry = int(carry)
            curr.next = ListNode(sum % 10)
            curr = curr.next;
            if (p != None):
                p = p.next
            if (q != None):
                q = q.next
        #print(type(carry))
        if (carry > 0):
            curr.next = ListNode(carry)
        return dummyHead.next
