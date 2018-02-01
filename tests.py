from morse import Morse, DotDash
import unittest

class MorseCodeTests(unittest.TestCase):
	""" unit tests for the reading, translation and representation of the
		Morse code class"""
	@classmethod
	def setUpClass(self):
		""" this sets up a class through each of the initiation methods, making
			sure they all work """
		self.morse_test1 = Morse(morse = '... --- ... / .----')
		self.morse_test2 = Morse(words = 'You... never did! - The Kenosha Kid')
		self.morse_test3 = Morse()
		self.morse_test3.read_words('cam was here')
		self.morse_test4 = Morse()
		self.morse_test4.read_morse('-.-. .- -- / -. ..- --. . -. -')
		self.morse_test5 = Morse()
		self.morse_test5.read(morse = '... --- ...')

	def test_encoding(self):
		""" make sure the translation from morse to words, 
			and words to morse have occured """
		self.assertEqual(self.morse_test1.words, 'sos 1')
		self.assertEqual(self.morse_test1.morse, '... --- ... / .----')
	
	def test_double_pass(self):
		with self.assertRaises(ValueError):
			self.morse_test5.read(words= 'we are passing two things ', morse = '... --- ...')

	def test_properties(self):
		""" make sure we can't overwrite the stored strings """
		with self.assertRaises(AttributeError):
			self.morse_test1.words = 'change the words'

		with self.assertRaises(AttributeError):
			self.morse_test1.morse = '... --- ...'

	def test_repr(self):
		""" make sure that __repr__ is printing the expected message 
			when print(object) is called. """
		self.assertEqual(self.morse_test2.__repr__(), 'message: you never did the kenosha kid\n-.-- --- ..- / -. . ...- . .-. / -.. .. -.. / - .... . / -.- . -. --- ... .... .- / -.- .. -..' )

#for dev
#test_test = MorseCodeTests()
#test_test.setUpClass()
#test_test.test_double_pass()
#test_test.test_encoding()
#test_test.test_properties()
#test_test.test_repr()

if __name__ == '__main__':

	unittest.main()
