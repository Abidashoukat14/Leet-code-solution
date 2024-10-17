class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        map_pattern={}
        map_words={}
        words=s.split()
        if len(words)!=len(pattern):
            return False
        for i in range(len(pattern)):
            letter=pattern[i]
            word=words[i]
            if letter not in map_pattern and word not in map_words:
                  map_pattern[letter]=word
                  map_words[word]=letter
            else:
                 if map_pattern.get(letter)!=word or map_words.get(word)!=letter:
                     return False
        return True

            
        