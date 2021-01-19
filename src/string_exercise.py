class StringExercise:

    def __init__(self):
        pass   # Do some initial setup in this constructor method, if needed

    def reverse_string(self, input_str):
        """
        Reverses order of characters in string input_str.
        """

        n = len(input_str)
        output_str= [' '] * n
        i=0
        j=n-1
        for ele in input_str:
            output_str[j] = ele
            j -= 1

        
        final_str = ""
        for st in output_str:
            final_str += st
        return final_str

    def is_english_vowel(self, character):
        """
        Returns True if character is an english vowel
        and False otherwise.
        """

        if character in('a','e','i','o','u','A','E','I','O','U'):
            return True
        else:
            return False
        return None

    def find_longest_word(self, sentence):
        """
        Returns the longest word in string sentence.
        In case there are several, return the first.
        """

        words = sentence.split(' ')
        max=0
        longest=""
        for word in words:
            if len(word) > max:
                max=len(word)
                longest=word
        return longest

    def get_word_lengths(self, text):
        """
        Returns a list of integers representing
        the word lengths in string text.
        """
        my_list = []
        words = text.split(' ')
        for word in words:
            my_list.append(len(word))
        return my_list


obj = StringExercise()
# print(obj.reverse_string("purvi"))
# print(obj.is_english_vowel('a'))
# print(obj.find_longest_word("the big brown fox"))
# print(obj.get_word_lengths("the big brown fox"))



