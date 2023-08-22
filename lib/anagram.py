# your code goes here!

# We're creating a special program for finding anagrams, which are words made by rearranging letters.
class Anagram:
    # This function runs automatically when we follow the steps to create a new 'Anagram'.
    def __init__(self, word):
        # We store the main word we want to find anagrams for so we can compare it later.
        self.word = word

    # This part of the class helps us find words that can be anagrams of our main word.
    def match(self, possible_anagrams):
        # We're setting up a list to put the anagrams we find in.
        matches = []
        
        # Now we're going through each word in the list of possible anagrams.
        for anagram in possible_anagrams:
            # We're checking if the letters of the main word and the possible anagram are the same when arranged in order.
            # Also, we're making sure the words are not exactly the same.
            if sorted(self.word.lower()) == sorted(anagram.lower()) and self.word.lower() != anagram.lower():
                # If the letters match when sorted and the words are different, we add this word to our list of matches.
                matches.append(anagram)
        
        # After looking through all possible anagrams, we give back the list of matches we found.
        return matches