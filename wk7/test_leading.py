import unittest
#import tools
from leading import leading_substrings

class Testleading(unittest.TestCase):
    '''Tests for leading_substrings()'''

    def test_leading_bear(self):
        '''Test an bear list.'''
        
        output= leading_substrings('bear')
        output_expected = ['b', 'be', 'bea', 'bear']
        self.assertEqual(output_expected, output, "'bear' is decomposed correctly.")
        
    def test_leading_empty(self):
        '''Test an empty list.'''
        
        output= leading_substrings('')
        output_expected = []
        
        self.assertEqual(output_expected, output, "'' is decomposed correctly.")
# other scenario




if __name__ == '__main__':
    unittest.main()
