from random import choice


class WordFinder:
    """WordFinder: finds random words from a dictionary.

    >>> wf = WordFinder("words.txt")
    235886 words read.
    
    """
    def __init__(self, file):
        """
        Instance creation
        file: holds file path
        word_list: creates empty list to be filled with words from file
        invokes and prints self.words_read(): to tell the user how many words were just read
        """
        self.file = file
        self.word_list = []
        print(self.words_read())

    def read_file(self):
        """wordfinder method to read all words in file and save to list"""
        with open(self.file, 'r') as file:
            content = file.readlines()
            for word in content:
                self.word_list.append(word)

    def words_read(self):
        """wordfinder method to print the number of words read"""
        self.read_file()
        return f"{len(self.word_list)} words read."
    
    def random(self):
        """wordfinder method to return a random word"""
        return choice(self.word_list).strip('\n')