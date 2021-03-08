#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

class AboutSets(Koan):
    def test_sets_make_keep_lists_unique(self):
        highlanders = ['MacLeod', 'Ramirez', 'MacLeod', 'Matunas', 'MacLeod', 'Malcolm', 'MacLeod']

        there_can_only_be_only_one = set(highlanders)

        self.assertEqual({'Malcolm', 'Ramirez', 'Matunas', 'MacLeod'}, there_can_only_be_only_one) # Lists converted to sets eliminates repeats.

    # def test_empty_sets_have_different_syntax_to_populated_sets(self):
    #     self.assertEqual(__, {1, 2, 3})
    #     self.assertEqual(__, set())

    def test_dictionaries_and_sets_use_same_curly_braces(self):
        # Note: Literal sets using braces were introduced in python 3.
        #       They were also backported to python 2.7.

        self.assertEqual(set, {1, 2, 3}.__class__)
        self.assertEqual(dict, {'one': 1, 'two': 2}.__class__)

        self.assertEqual(dict, {}.__class__) # dict is the default for nothing in it

    def test_creating_sets_using_strings(self):
        self.assertEqual({'12345'}, {'12345'})
        self.assertEqual({'1', '2', '3', '4', '5'}, set('12345')) # set makes every character in a string into an item in a set

    def test_convert_the_set_into_a_list_to_sort_it(self):
        self.assertEqual(['1', '2', '3', '4', '5'], sorted(set('12345'))) # sorted function turns a set into a list

    # ------------------------------------------------------------------

    def test_set_have_arithmetic_operators(self):
        scotsmen = {'MacLeod', 'Wallace', 'Willie'}
        warriors = {'MacLeod', 'Wallace', 'Leonidas'}

        self.assertEqual({'Willie'}, scotsmen - warriors) # returns only Willie because it subtracts the others
        self.assertEqual({'Leonidas', 'MacLeod', 'Willie', 'Wallace'}, scotsmen | warriors) # Pipe operator gives all items that appear in both
        self.assertEqual({'MacLeod', 'Wallace'}, scotsmen & warriors) # & operator gives only the ones that appear in both
        self.assertEqual({'Leonidas', 'Willie'}, scotsmen ^ warriors) # ^ will give back those that do not appear in both

    # ------------------------------------------------------------------

    def test_we_can_query_set_membership(self):
        self.assertEqual(True, 127 in {127, 0, 0, 1} )
        self.assertEqual(True, 'cow' not in set('apocalypse now') ) # Because the string doesn't appear in a set full of one-character strings

    def test_we_can_compare_subsets(self):
        self.assertEqual(True, set('cake') <= set('cherry cake')) # length is less than or equal to the other set
        self.assertEqual(True, set('cake').issubset(set('cherry cake')) ) # is a subset of that other set

        self.assertEqual(False, set('cake') > set('pie')) # cake has more letters than pie....??????
