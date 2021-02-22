#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutStrings(Koan):

    def test_double_quoted_strings_are_strings(self):
        string = "Hello, world."
        # Strings can be in quotes
        self.assertEqual(True, isinstance(string, str))

    def test_single_quoted_strings_are_also_strings(self):
        string = 'Goodbye, world.'
        # Or in apostrophes
        self.assertEqual(True, isinstance(string, str))

    def test_triple_quote_strings_are_also_strings(self):
        string = """Howdy, world!"""
        # Or in triple quotes. Triple quotes allows multiple lines
        self.assertEqual(True, isinstance(string, str))

    def test_triple_single_quotes_work_too(self):
        string = '''Bonjour tout le monde!'''
        # Triple apostrophes also allows multiple lines
        self.assertEqual(True, isinstance(string, str))

    def test_raw_strings_are_also_strings(self):
        string = r"Konnichi wa, world!"
        # Raw strings can be used in regex
        self.assertEqual(True, isinstance(string, str))

    def test_use_single_quotes_to_create_string_with_double_quotes(self):
        string = 'He said, "Go Away."'
        # Here, we use the escape key to escape the quotation mark
        self.assertEqual("He said, \"Go Away.\"", string)

    def test_use_double_quotes_to_create_strings_with_single_quotes(self):
        string = "Don't"
        # Same as above, but we escape the apostrophe
        self.assertEqual('Don\'t', string)

    def test_use_backslash_for_escaping_quotes_in_strings(self):
        a = "He said, \"Don't\""
        b = 'He said, "Don\'t"'
        # They are both the same, because they are just different ways of saying the same thing. See above explanations for more info
        self.assertEqual(True, (a == b))

    def test_use_backslash_at_the_end_of_a_line_to_continue_onto_the_next_line(self):
        string = "It was the best of times,\n\
It was the worst of times."
        # Not sure why it wanted me to give the length...? But yeah, the backslash by itself and \n can be used as newline keys
        self.assertEqual(52, len(string))

    def test_triple_quoted_strings_can_span_lines(self):
        string = """
Howdy,
world!
"""
        #Again not sure why it wanted the length, but triple quotes can be used for newlines.
        self.assertEqual(15, len(string))

    def test_triple_quoted_strings_need_less_escaping(self):
        a = "Hello \"world\"."
        b = """Hello "world"."""
        # These are the same because triple quotes and single quotes don't make any difference internally as far as the actual content of a string.
        self.assertEqual(True, (a == b))

    def test_escaping_quotes_at_the_end_of_triple_quoted_string(self):
        string = """Hello "world\""""
        # This can be used to escape ending a triple quote earlier than expected, i.e. printing out "Hello "world"" instead of SYNTAXERROR
        self.assertEqual("Hello \"world\"", string)

    def test_plus_concatenates_strings(self):
        string = "Hello, " + "world"
        # + can be used to concantenate (: a string.
        self.assertEqual("Hello, world", string)

    def test_adjacent_strings_are_concatenated_automatically(self):
        string = "Hello" ", " "world"
        # Spacing can also be used to concantenate a string.
        self.assertEqual("Hello, world", string)

    def test_plus_will_not_modify_original_strings(self):
        hi = "Hello, "
        there = "world"
        string = hi + there
        # Strings are immutable so cannot be modified by any means at all
        self.assertEqual("Hello, ", hi)
        self.assertEqual("world", there)

    def test_plus_equals_will_append_to_end_of_string(self):
        hi = "Hello, "
        there = "world"
        hi += there
        # += can also be used as a shorthand to combine the initial string with a second one.
        self.assertEqual("Hello, world", hi)

    def test_plus_equals_also_leaves_original_string_unmodified(self):
        original = "Hello, "
        hi = original
        there = "world"
        hi += there
        # Even if you make a clone of it, it still won't change the original. It will just copy it to another variable.
        self.assertEqual("Hello, ", original)

    def test_most_strings_interpret_escape_characters(self):
        string = "\n"
        # \n in a string evaluates to one single character, but it is a whitespace character.
        self.assertEqual('\n', string)
        self.assertEqual("""\n""", string)
        self.assertEqual(1, len(string))
