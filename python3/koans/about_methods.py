#!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Partially based on AboutMethods in the Ruby Koans
#

from runner.koan import *

def my_global_function(a,b):
    return a + b

class AboutMethods(Koan):
    def test_calling_a_global_function(self):
        self.assertEqual(5, my_global_function(2,3)) #5 is what the function would return

    # NOTE: Wrong number of arguments is not a SYNTAX error, but a
    # runtime error.
    def test_calling_functions_with_wrong_number_of_arguments(self):
        try:
            my_global_function()
        except TypeError as exception:
            msg = exception.args[0]

        # Note, the text comparison works for Python 3.2
        # It has changed in the past and may change in the future
        self.assertRegex(msg,
            r'my_global_function\(\) missing 2 required positional arguments')

        try:
            my_global_function(1, 2, 3)
        except Exception as e:
            msg = e.args[0]

        # Note, watch out for parenthesis. They need slashes in front!
        self.assertRegex(msg, r"my_global_function\(\) takes 2 positional arguments but 3 were given") # In regular expressions, () normally mean "parse this", but if you escape them, then it doesn't do that

    # ------------------------------------------------------------------

    def pointless_method(self, a, b):
        sum = a + b

    def test_which_does_not_return_anything(self):
        self.assertEqual(None, self.pointless_method(1, 2)) # self in this function is not the same as self in the pointless_method function, so it returns none, because no value is attributed to it
        # Notice that methods accessed from class scope do not require
        # you to pass the first "self" argument?

    # ------------------------------------------------------------------

    def method_with_defaults(self, a, b='default_value'):
        return [a, b]

    def test_calling_with_default_values(self):
        self.assertEqual([1, 'default_value'], self.method_with_defaults(1)) # A default value will be how it is if no other value is attributed to it
        self.assertEqual([1, 2], self.method_with_defaults(1, 2)) # But if you override it it will change.

    # ------------------------------------------------------------------

    def method_with_var_args(self, *args):
        return args

    def test_calling_with_variable_arguments(self):
        self.assertEqual((), self.method_with_var_args()) # A * before args always returns a tuple
        self.assertEqual(('one',), self.method_with_var_args('one'))
        self.assertEqual(('one', 'two'), self.method_with_var_args('one', 'two'))

    # ------------------------------------------------------------------

    def function_with_the_same_name(self, a, b):
        return a + b

    def test_functions_without_self_arg_are_global_functions(self):
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(12, function_with_the_same_name(3,4)) # local functions trump global functions

    def test_calling_methods_in_same_class_with_explicit_receiver(self):
        def function_with_the_same_name(a, b):
            return a * b

        self.assertEqual(7, self.function_with_the_same_name(3,4)) # But if you say SELF you're referring to the class you're in, so that would be the global (class) function

    # ------------------------------------------------------------------

    def another_method_with_the_same_name(self):
        return 10

    link_to_overlapped_method = another_method_with_the_same_name

    def another_method_with_the_same_name(self):
        return 42

    def test_that_old_methods_are_hidden_by_redefinitions(self):
        self.assertEqual(42, self.another_method_with_the_same_name()) # The last definition of a function is the one that stays

    def test_that_overlapped_method_is_still_there(self):
        self.assertEqual(10, self.link_to_overlapped_method()) # but if you put the previous definition of a function into a variable, it is saved within that variable

    # ------------------------------------------------------------------

    def empty_method(self):
        pass

    def test_methods_that_do_nothing_need_to_use_pass_as_a_filler(self):
        self.assertEqual(None, self.empty_method()) # If a method does nothing (uses pass) it returns None if you ever call it for anything

    def test_pass_does_nothing_at_all(self):
        "You"
        "shall"
        "not"
        pass
        self.assertEqual(True, "Still got to this line" != None) # "You" on its own is tantamount to a comment. Strings by themselves are often used as comments by coders but this is a discouraged practice. What "KSDfhokdfkho" on its own really is telling the code is "KSDfhokdfkho" = True. And the code is like "Uh, yeah. Duh" and moves on. Pass doesn't exit anything. It just does nothing. In fact, watch this:
        pass
        pass
        pass
        pass
        pass
        # See? Nothing broke, it just doesn't do anything

    # ------------------------------------------------------------------

    def one_line_method(self): return 'Madagascar'

    def test_no_indentation_required_for_one_line_statement_bodies(self):
        self.assertEqual("Madagascar", self.one_line_method()) # I like to move it, move it! (One-line stuff works)

    # ------------------------------------------------------------------

    def method_with_documentation(self):
        "A string placed at the beginning of a function is used for documentation"
        return "ok"

    def test_the_documentation_can_be_viewed_with_the_doc_method(self):
        self.assertRegex(self.method_with_documentation.__doc__, "A string placed at the beginning of a function is used for documentation") # Okay so I guess then that documentation with strings really was intended by the developers of Python itself.

    # ------------------------------------------------------------------

    class Dog:
        def name(self):
            return "Fido"

        def _tail(self):
            # Prefixing a method with an underscore implies private scope
            return "wagging"

        def __password(self):
            return 'password' # Genius!

    def test_calling_methods_in_other_objects(self):
        rover = self.Dog()
        self.assertEqual("Fido", rover.name()) # You can call a method of a class outside the class itself

    def test_private_access_is_implied_but_not_enforced(self):
        rover = self.Dog()

        # This is a little rude, but legal
        self.assertEqual("wagging", rover._tail()) # You can (but probably shouldn't) call an in-scope method.

    def test_attributes_with_double_underscore_prefixes_are_subject_to_name_mangling(self):
        rover = self.Dog()
        with self.assertRaises(AttributeError): password = rover.__password() # This can't be done...for some reason

        # But this still is!
        self.assertEqual("password", rover._Dog__password()) # And this...can...be done?...I'm not really sure

        # Name mangling exists to avoid name clash issues when subclassing.
        # It is not for providing effective access protection
