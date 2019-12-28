import unittest

from credit_card.masker import mask_number


class TestCarMasking(unittest.TestCase):

	def test_various_inputs(self):
		test_cases = [ 
			{'input': '4556364607935616','output': '4556########5616'}, 
			{'input': '4556-3646-0793-5616', 'output': '4556-####-####-5616'}, 
			{'input': '64607935616', 'output': '6460###5616'}, 
			{'input': 'ABCD-EFGH-IJKLM-NOPQ', 'output': 'ABCD-EFGH-IJKLM-NOPQ'}, 
			{'input': '', 'output': ''}, 
			{'input': 'A1234567BCDEFG89HI', 'output': 'A123####BCDEFG89HI'}, 
			{'input': 'Skippy', 'output': 'Skippy'} 
		]

		for test_case in test_cases:
			self.assertEqual(
				mask_number(test_case['input']),
				test_case['output'])


if __name__ == '__main__':
	unittest.main()
