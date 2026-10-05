class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        words = s.split()

        # Pattern letters and words count should be same
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}

        for i in range(len(pattern)):

            char = pattern[i]
            word = words[i]

            # Check character already has a different word
            if char in char_to_word:
                if char_to_word[char] != word:
                    return False

            # Check word already has a different character
            if word in word_to_char:
                if word_to_char[word] != char:
                    return False

            # Store the mapping
            char_to_word[char] = word
            word_to_char[word] = char

        return True