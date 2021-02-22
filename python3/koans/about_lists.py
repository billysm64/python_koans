#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutArrays in the Ruby Koans
#

from runner.koan import *

class AboutLists(Koan):
    def test_creating_lists(self):
        empty_list = list()
        # list() returns a list with 0 items
        self.assertEqual(list, type(empty_list))
        self.assertEqual(0, len(empty_list))

    def test_list_literals(self):
        nums = list()
        self.assertEqual([], nums)

        nums[0:] = [1]
        self.assertEqual([1], nums)

        nums[1:] = [2]
        self.assertListEqual([1, 2], nums)
        # splicing can be used to add to lists
        nums.append(333)
        self.assertListEqual([1, 2, 333], nums)
        # Append will put in the thing you tell it to at the end of a list

    def test_accessing_list_elements(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        # Negatives go backward in a list, positives go forward.
        self.assertEqual('peanut', noms[0])
        self.assertEqual('jelly', noms[3])
        self.assertEqual('jelly', noms[-1])
        self.assertEqual('butter', noms[-3])

    def test_slicing_lists(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        # [beginning : end : IndexJump]
        self.assertEqual(['peanut'], noms[0:1])
        self.assertEqual(['peanut', 'butter'], noms[0:2])
        self.assertEqual([], noms[2:2]) #2:2 does nothing because start at 2 end at 2
        self.assertEqual(['and', 'jelly'], noms[2:20])
        self.assertEqual([], noms[4:0]) #nothing at index 4
        self.assertEqual([], noms[4:100]) #there is no index 4
        self.assertEqual([], noms[5:0]) # no index 5

    def test_slicing_to_the_edge(self):
        noms = ['peanut', 'butter', 'and', 'jelly']
        # put nothing after/before : means everything before/after :
        self.assertEqual(['and', 'jelly'], noms[2:])
        self.assertEqual(['peanut', 'butter'], noms[:2])

    def test_lists_and_ranges(self):
        self.assertEqual(range, type(range(5)))
        self.assertNotEqual([1, 2, 3, 4, 5], range(1,6))
        # ranges give every number except the max, including 0
        self.assertEqual([0, 1, 2, 3, 4], list(range(5)))
        self.assertEqual([5, 6, 7, 8], list(range(5, 9)))

    def test_ranges_with_steps(self):
        self.assertEqual([5, 4], list(range(5, 3, -1))) ##iterates backwards
        self.assertEqual([0, 2, 4, 6], list(range(0, 8, 2))) #skips 2 every time
        self.assertEqual([1, 4, 7], list(range(1, 8, 3))) #skip 3
        self.assertEqual([5, 1, -3], list(range(5, -7, -4))) #goes back 4 every time
        self.assertEqual([5, 1, -3, -7], list(range(5, -8, -4))) #goes back 4 every time

    def test_insertions(self):
        knight = ['you', 'shall', 'pass']
        knight.insert(2, 'not') #inserts at position 2
        self.assertEqual(['you', 'shall', 'not', 'pass'], knight)

        knight.insert(0, 'Arthur') #inserts at beginning
        self.assertEqual(['Arthur', 'you', 'shall', 'not', 'pass'], knight)

    def test_popping_lists(self):
        stack = [10, 20, 30, 40]
        stack.append('last') #append will add to the end of a list

        self.assertEqual([10, 20, 30, 40, 'last'], stack)

        popped_value = stack.pop() #will automatically delete the last one, return value of the thing popped
        self.assertEqual('last', popped_value)
        self.assertEqual([10, 20, 30, 40], stack)

        popped_value = stack.pop(1) # you can pop a specific index this way
        self.assertEqual(20, popped_value)
        self.assertEqual([10, 30, 40], stack)

        # Notice that there is a "pop" but no "push" in python?

        # Part of the Python philosophy is that there ideally should be one and
        # only one way of doing anything. A 'push' is the same as an 'append'.

        # To learn more about this try typing "import this" from the python
        # console... ;)

    def test_making_queues(self):
        queue = [1, 2]
        queue.append('last') #this appended to the end of the list

        self.assertEqual([1, 2, 'last'], queue)

        popped_value = queue.pop(0) #this popped index 0
        self.assertEqual(1, popped_value)
        self.assertEqual([2, 'last'], queue)

        # Note, popping from the left hand side of a list is
        # inefficient. Use collections.deque instead.
