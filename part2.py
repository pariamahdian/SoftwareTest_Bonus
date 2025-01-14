import unittest
from unittest.mock import patch
from part1 import InputDomainModeler, generate_model

class TestGenerateModel(unittest.TestCase):

    def setUp(self):
        char1 = 'A'
        block1 = ['a1', 'a2']
        self.obj1 = InputDomainModeler(char1, block1)
        
        char2 = 'B'
        block2 = ['b1', 'b2']
        self.obj2 = InputDomainModeler(char2, block2)
        
        char3 = 'C'
        block3 = ['c1', 'c2', 'c3']
        self.obj3 = InputDomainModeler(char3, block3)
        
        char4 = 'D'
        block4 = ['d1', 'd2']
        self.obj4 = InputDomainModeler(char4, block4)

    def test_generate_model_invalid_mode(self):
        with patch('builtins.input', return_value='invalid'):
            with patch('builtins.print') as mock_print:
                objects = [self.obj1, self.obj2, self.obj3, self.obj4]
                generate_model(objects, 'invalid')
                mock_print.assert_called_with("invalid mode")

    def test_generate_model_BCC_mode(self):
        with patch('builtins.print') as mock_print:
            objects = [self.obj1, self.obj2, self.obj3, self.obj4]
            generate_model(objects, 'BCC')
            self.assertEqual(mock_print.call_count, 6)  # Adjust based on the actual expected output

    def test_generate_model_ACoC_mode(self):
        with patch('builtins.print') as mock_print:
            objects = [self.obj1, self.obj2, self.obj3, self.obj4]
            generate_model(objects, 'ACoC')
            self.assertEqual(mock_print.call_count, 23)  # Adjust based on the actual expected output

    def test_generate_model_ECC_mode(self):
        with patch('builtins.print') as mock_print:
            objects = [self.obj1, self.obj2, self.obj3, self.obj4]
            generate_model(objects, 'ECC')
            self.assertEqual(mock_print.call_count, 3)  # Adjust based on the actual expected output

if __name__ == '__main__':
    unittest.main()