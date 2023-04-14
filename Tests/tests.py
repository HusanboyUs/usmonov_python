from unittest import TestCase
from unittest.mock import patch
import unittest
from random import randint

#modified function for testing
num_checker = lambda number: "Привет" if number > 7 else None

class TestNumber(TestCase):
    def test_correct_answer(self):
        lower_digits=randint(0,6)
        result = num_checker(lower_digits)
        self.assertIsNone(result)

    def test_correct_answer(self):
        bigger_numbers=randint(7,100)
        result = num_checker(bigger_numbers)
        self.assertEqual(result,'Привет')

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            result = num_checker('sss')


#modified function for testing
def checkName():
    username=input('Hello, what is your name? ')
    if username in ['Вячеслав','вячеслав']:
        return 'Привет, {}'.format(username)
    else:
        return 'Нет такого имени'



class TestCheckName(TestCase):

    @patch('builtins.input', return_value='Vlad')
    def test_wrong_answer(self,mock_input):
        result = checkName()
        self.assertEqual(result, 'Нет такого имени')

    @patch('builtins.input', return_value='Вячеслав')
    def test_correct_asnwer(self,mock_input):
        result = checkName()
        self.assertEqual(result, 'Привет, Вячеслав') 

    @patch('builtins.input', return_value=345)
    def test_digit_asnwer(self,mock_input):
        result = checkName()
        self.assertEqual(result, 'Нет такого имени') 


#modifed function for testing


def num_multiples():
    result=[]
    user_numbers=list(input('Please enter your sequential numbers: '))
    for nums in user_numbers:
        if int(nums) %3==0:
            result.append(nums)
        else:
            return None
            #number cannot be divded 3 evenly
        return result    
        

class TestNumberMultipler(TestCase):

    @patch('builtins.input', return_value='2344')
    def test_incorrect_answer(self,mock_input):
        result = num_multiples()
        self.assertEqual(result, None)

    @patch('builtins.input', return_value='369')
    def test_correct_response(self,mock_input):
        result = num_multiples()
        self.assertEqual(result, ['3'])

    @patch('builtins.input', return_value='dsdsad')
    def test_wrong_input(self,mock_input):
        with self.assertRaises(ValueError):
            result = num_multiples()    



if __name__ == '__main__':
    unittest.main()
