#!/usr/bin/python3

import unittest
import pep8
from models.user import User

class User_testing(unittest.TestCase):
    

    def testpep8(self):
        #test codestyle """
        pepstylecode = pep8.StyleGuide(quiet=True)
        path_user = 'models/user.py'
        result = pepstylecode.check_files([path_user])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors.")