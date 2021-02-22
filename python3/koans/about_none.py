#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Based on AboutNil in the Ruby Koans
#

from runner.koan import *

class AboutNone(Koan):

    def test_none_is_an_object(self):
        "Unlike NULL in a lot of languages"
        # None is a type of object
        self.assertEqual(True, isinstance(None, object))

    def test_none_is_universal(self):
        "There is only one None"
        # None is the only None there is, and there can't be another None because there just can't be, it isn't possible. It would break a hole in the time-space continuum for Null or Undefined to be extra things in Python.
        self.assertEqual(True, None is None)

    def test_what_exception_do_you_get_when_calling_nonexistent_methods(self):
        """
        What is the Exception that is thrown when you call a method that does
        not exist?

        Hint: launch python command console and try the code in the block below.

        Don't worry about what 'try' and 'except' do, we'll talk about this later
        """
        try:
            None.some_method_none_does_not_know_about()
        except Exception as ex:
            ex2 = ex

        # What exception has been caught?
        #
        # Need a recap on how to evaluate __class__ attributes?
        #
        #     https://github.com/gregmalcolm/python_koans/wiki/Class-Attribute
        self.assertEqual(AttributeError, ex2.__class__)

        # What message was attached to the exception?
        # (HINT: replace __ with part of the error message.)
        self.assertRegex(ex2.args[0], "NoneType")

        # AttributeError is a type of error that evaluates to the same as something that gets that exact same error.
        #NoneType is in a list called ex2.args because it is one thing that does not have any methods. None can't do anything but be None and that's the only thing it's ever been able to be.

    def test_none_is_distinct(self):
        """
        None is distinct from other things which are False.
        """
        # None is the only thing that evaluates to None—not 0 or False or an empty string or any of that.
        self.assertEqual(True, None is not 0)
        self.assertEqual(True, None is not False)
