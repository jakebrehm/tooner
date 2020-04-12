# -*- coding: utf-8 -*-

'''
multitooner.launcher unit test
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Unit test of the launcher module of Multitooner.
'''

import unittest

import multitooner.launcher


class TestAnalyze(unittest.TestCase):
    '''Unit test the analyze module.'''

    def test_failed_connection_due_to_incorrect_login(self):
        '''Tests the ToontownLauncher._connect method in the failure
        case due to incorrect login credentials.'''

        # Initialize a ToontownLauncher object with a dummy install directory
        launcher = multitooner.launcher.ToontownLauncher('')
        response = launcher._make_request({
            'username': 'test', 
            'password': 'test',
        })
        expected = {
            'success': 'false',
            'banner': 'Incorrect username and/or password.',
        }
        self.assertEqual(response, expected)


if __name__ == '__main__':
    unittest.main()
