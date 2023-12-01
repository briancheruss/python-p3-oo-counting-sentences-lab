#!/usr/bin/env python3

import re

class MyString:
    pass
    def __init__(self, value=""):
        if not isinstance(value, str):
            raise ValueError("The value must be a string.")
        self.value = value

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Split the string on punctuation and filter out empty strings
        sentences = [s.strip() for s in re.split(r'[.!?]', self.value) if s.strip()]
        return len(sentences)

# Example usage:
string = MyString("This is a string! It has three sentences. Right?")
print(string.is_sentence())    # Should print True
print(string.is_question())    # Should print False
print(string.is_exclamation())  # Should print False
print(string.count_sentences())  # Should print 3
