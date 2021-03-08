#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStringManipulation(Koan):

    def test_use_format_to_interpolate_variables(self):
        value1 = 'one'
        value2 = 2
        string = "The values are {0} and {1}".format(value1, value2)
        self.assertEqual("The values are one and 2", string) # .format takes {1} and {2} and passes in the specified values

    def test_formatted_values_can_be_shown_in_any_order_or_be_repeated(self):
        value1 = 'doh'
        value2 = 'DOH'
        string = "The values are {1}, {0}, {0} and {1}!".format(value1, value2)
        self.assertEqual("The values are DOH, doh, doh and DOH!", string) # they can repeat too

    def test_any_python_expression_may_be_interpolated(self):
        import math # import a standard python module with math functions

        decimal_places = 4
        string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5),
            decimal_places)
        self.assertEqual("The square root of 5 is 2.2361", string) # Format in this case takes the square root of 5 and puts in the amount of decimal places you want

    def test_you_can_get_a_substring_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("let", string[7:10]) # This splices out starting at 7 from beginning and ending at 10 from beginning

    def test_you_can_get_a_single_character_from_a_string(self):
        string = "Bacon, lettuce and tomato"
        self.assertEqual("a", string[1]) # This gives you the second item in the string, which is a

    def test_single_characters_can_be_represented_by_integers(self):
        self.assertEqual(97, ord('a')) # ord gives you the number representing the unicode number of a specific letter
        self.assertEqual(True, ord('b') == (ord('a') + 1)) #they appear in order

    def test_strings_can_be_split(self):
        string = "Sausage Egg Cheese"
        words = string.split()
        self.assertListEqual(['Sausage', 'Egg', 'Cheese'], words) #words.split takes everything in a string, and by default will split it by spaces

    def test_strings_can_be_split_with_different_patterns(self):
        import re #import python regular expression library

        string = "the,rain;in,spain"
        pattern = re.compile(',|;') #This makes a custom rule for .split, meaning "split by , or ;"

        words = pattern.split(string)

        self.assertListEqual(['the', 'rain', 'in', 'spain'], words)

        # Pattern is a Python regular expression pattern which matches ',' or ';'

    def test_raw_strings_do_not_interpret_escape_characters(self):
        string = r'\n' # r'' stands for raw. It can make characters compile as what you typed them as even in cases of escapes
        self.assertNotEqual('\n', string)
        self.assertEqual("\\n", string) # \\ can escape an escaper
        self.assertEqual(2, len(string)) # It represents a string literally containing backslash n, meaning that is 2 characters long

        # Useful in regular expressions, file paths, URLs, etc.

    def test_strings_can_be_joined(self):
        words = ["Now", "is", "the", "time"]
        self.assertEqual("Now is the time", ' '.join(words)) # ' '.join will join the list together into a string, with a space between everything

    def test_strings_can_change_case(self):
        self.assertEqual("Guido", 'guido'.capitalize()) # capitalizes the first letter
        self.assertEqual("GUIDO", 'guido'.upper()) #capitalizes everything
        self.assertEqual("timbot", 'TimBot'.lower()) #lowercases everything
        self.assertEqual("Guido Van Rossum", 'guido van rossum'.title()) # does title case
        self.assertEqual("tOtAlLy AwEsOmE", 'ToTaLlY aWeSoMe'.swapcase()) # swaps the lowers for the uppers
