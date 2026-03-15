class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # Create a dummy node to serve as the head of the result list
        current = dummy  # Initialize a pointer to build the result list
        carry = 0  # Initialize the carry to 0

        while l1 is not None or l2 is not None:  # Traverse both lists
            x = l1.val if l1 is not None else 0  # Get the value of the current node in l1, or 0 if l1 is null
            y = l2.val if l2 is not None else 0  # Get the value of the current node in l2, or 0 if l2 is null
            sum = carry + x + y  # Calculate the sum of the current values and the carry
            carry = sum // 10  # Update the carry
            current.next = ListNode(sum % 10)  # Create a new node with the digit value and link it to the result list
            current = current.next  # Move to the next node in the result list

            if l1 is not None: l1 = l1.next  # Move to the next node in l1
            if l2 is not None: l2 = l2.next  # Move to the next node in l2

        if carry > 0:  # If there is a remaining carry, create a new node for it
            current.next = ListNode(carry)

        return dummy.next  # Return the head of the result list
