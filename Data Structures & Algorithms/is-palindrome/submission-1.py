class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = []

        for letter in s.lower():
            if letter.isalnum():
                sentence.append(letter)    

        return sentence[::-1]  == sentence
        


       
        