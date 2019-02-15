# -*- coding: utf-8 -*-
# test the c_parse module/library
import sys
import unittest
from mock import patch
from c_parse.c_parse import CommandLineParser

# test the c_parse module
class Test_c_parse_0(unittest.TestCase):
	def setUp(self):
		self.commands = CommandLineParser()
		self.commands.addArgument('-f',help_text = "file")
		self.commands.addArgument('-p',help_text = "update/patch")
		self.commands.addArgument('-d',help_text = "delete/remove")
		self.commands.addArgument('-h',help_text = "show help")

	def test_str_function(self):
		expected = 'CommandLineParser object'
		self.assertEqual(self.commands.__str__(),expected)

	def test_repr_function(self):
		expected = 'CommandLineParser object'
		self.assertEqual(self.commands.__repr__(),expected)

	def test_addArgument(self):
		expected = '-f'
		self.assertEqual(self.commands.addArgument('-f'),expected)

	#--------------------------------------------------------------------
	# test formatCommands with command line arguments
	def test_formatCommands_0(self):
		test_args = ["test.py","-f","/images/flower.png","-p","/images/flowers.png"]
		expected = ["-f /images/flower.png","-p /images/flowers.png"]
		with patch.object(sys,'argv',test_args):
			self.assertEqual(self.commands.formatCommands(),expected)

	# test formatCommands without command line arguments
	def test_formatCommands_1(self):
		test_args = ["test.py"]
		expected = False
		with patch.object(sys,'argv',test_args):
			self.assertEqual(self.commands.formatCommands(),expected)

	# test formatCommands with one single argument
	def test_formatCommands_2(self):
		test_args = ["test.py","-f"]
		expected = ['-f 0']
		with patch.object(sys,'argv',test_args):
			self.assertEqual(self.commands.formatCommands(),expected)

	# test formatCommands with many single argument
	def test_formatCommands_3(self):
		test_args = ["test.py","-f","-h"]
		expected = ['-f 0','-h 0']
		with patch.object(sys,'argv',test_args):
			self.assertEqual(self.commands.formatCommands(),expected)
	#--------------------------------------------------------------------
	# test parseArguments with command line arguments
	def test_parseArguments_0(self):
		test_args = ["test.py","-f","/images/flower.png"]
		expected = (True,{"-f":"/images/flower.png"})
		with patch.object(sys,'argv',test_args):
			self.commands.formatCommands()
			self.assertEqual(self.commands.parseArguments(),expected)

	# test parseArguments without command line arguments
	def test_parseArguments_1(self):
		test_args = ["test.py"]
		expected = False
		with patch.object(sys,'argv',test_args):
			self.commands.formatCommands()
			self.assertEqual(self.commands.parseArguments(),expected)
	#--------------------------------------------------------------------
	# test get_argumentsDict
	def test_get_argumentsDict(self):
		test_args = ["test.py","-f","/images/flower.png"]
		expected = {"-f":"/images/flower.png"}
		with patch.object(sys,'argv',test_args):
			self.commands.parseArguments()
			self.assertEqual(self.commands.get_argumentsDict(),expected)
	#--------------------------------------------------------------------
	# test get_helpTexts
	def test_get_helpTexts(self):
		expected = ['file','update/patch','delete/remove','show help']
		self.assertEqual(self.commands.get_helpTexts(),expected)

	# test get_argsKeys
	def test_get_argsKeys(self):
		test_args = ["test.py",'-p','update.exe',"-f","/images/flower.png",'-d','help.txt']
		expected = ['-d','-f','-p']
		with patch.object(sys,'argv',test_args):
			self.commands.parseArguments()
			self.assertEqual(self.commands.get_argsKeys(),expected)

	# test get_argsValues 
	def test_get_argsValues(self):
		test_args = ["test.py","-f","/images/flower.png",'-d','help.txt']
		expected = ['help.txt','/images/flower.png']
		with patch.object(sys,'argv',test_args):
			self.commands.parseArguments()
			self.assertEqual(self.commands.get_argsValues(),expected)
	
	def tearDown(self):
		del self.commands

class Test_c_parse_1(unittest.TestCase):
	def setUp(self):
		self.commands = CommandLineParser()

	# test get_helpTexts with a blank list
	def test_get_helpTexts(self):
		expected = False
		self.assertEqual(self.commands.get_helpTexts(),expected)
	
	def tearDown(self):
		del self.commands

if __name__ == '__main__':
	unittest.main()











