class Solution:
    def isPalindrome(self, x: int) -> bool:
        number = str(x)
        reversed_number = ""
        for i in number[ : : -1]:
            reversed_number += i

        if(number == reversed_number):
            return True
        else:
            return False