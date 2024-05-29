class Anagram:
    def __init__(self,word):
       self.word = word
    def match(self, text):
        return [word for word in text if sorted(word) == sorted(self.word)]
        
    pass
    