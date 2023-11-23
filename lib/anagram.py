# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word.lower()

    def is_anagram(self,enteredWord):
        return  sorted(enteredWord.lower())==sorted(self.word)
        

    def match(self,anagrams_list):
        return [anagram for anagram in anagrams_list if self.is_anagram(anagram) ]
        