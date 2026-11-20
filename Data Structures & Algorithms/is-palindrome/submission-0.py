class Solution:
    def isPalindrome(self, s: str) -> bool:
        sentence = []
        reverse = []

        for letter in s.lower():
            if letter.isalnum():
                sentence.append(letter)    
        print(sentence)

        for letter in range(len(sentence) - 1,-1 , -1):
            reverse.append(sentence[letter])

        return reverse == sentence
        


       
        