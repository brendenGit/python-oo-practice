from word_finder import WordFinder
from random import choice

class SpecialWordFinder(WordFinder):
    """SpecialWordFinder: extends WordFinder but has a special case for returning random words.
    - It will not return words that start with '#' or an emtpy line

    >>> swf = WordFinder("special_words.txt")
    11 words read.

    >>> value = swf.random()
    >>> value.startswith('#')
    False
    >>> value.startswith('\\n')
    False
    
    """
    def __init__(self, file):
        super().__init__(file)

    def random(self):
        while True:
            random_word = choice(self.word_list)
            if not random_word.startswith('#') and not random_word.startswith('\n'):
                return random_word.strip('\n')