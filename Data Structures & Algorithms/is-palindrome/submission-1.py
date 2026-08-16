class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstring = "" # this is a new str, which is emtpy and here we are not adding characters that are not alphanumeric

        for c in s:
            if c.isalnum():   #isalum is a built func 
                newstring += c.lower()  #adding charcater c which is in str s to newstring coz it is alphanumeric in lowercase
        return newstring == newstring[::-1]  #comparing the newstring and reverse str. [::-1] is the sytex for reveres str

        