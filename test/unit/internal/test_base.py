######################################################################
#
# File: test/unit/internal/test_base.py
#
# Copyright 2020 Backblaze Inc. All Rights Reserved.
#
# License https://www.backblaze.com/using_b2_code.html
#
######################################################################

from contextlib import contextmanager
import re
import unittest


class TestBase(unittest.TestCase):
    @contextmanager
    def assertRaises(self, exc, msg=None):
        try:
            yield
        except exc as e:
            if msg is not None and msg != str(e):
                assert False, "expected message '%s', but got '%s'" % (msg, str(e))
        else:
            assert False, f'should have thrown {exc}'

    @contextmanager
    def assertRaisesRegexp(self, expected_exception, expected_regexp):
        try:
            yield
        except expected_exception as e:
            if not re.search(expected_regexp, str(e)):
                assert False, "expected message '%s', but got '%s'" % (expected_regexp, str(e))
        else:
            assert False, f'should have thrown {expected_exception}'
