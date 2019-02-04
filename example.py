# -*- coding: utf-8 -*-
# example 

from c_parse.c_parse import CommandLineParser

# usage: python example.py -f ex/ex.txt prints the file content
#		 python example.py -h show help page
# in c_parse arguments are optional by default
# will print out the content of a file passed in as argument
class Example(object):
	def __init__(self):
		# instantiate the CommandLineParser class
		self.commands = CommandLineParser() # step 01
		# add the acceptable arguments for our command line program
		self.add_arguments() # step 02
		# parse the arguments,if successful return True and arguments dictionary(True,{'-f':'folder/example.txt'}) 
		# returns False if something went wrong
		self.response = self.parse_arguments() # step 03
		#print (self.response)
	
	def __str__(self):
		return 'Example object'
		
	def __repr__(self):
		return 'Example object'
		
	# step 02
	def add_arguments(self):
		self.file = self.commands.addArgument('-f',help_text = 'the file to read the content from')
		self.help = self.commands.addArgument('-h',help_text = 'show help')
			
	# step 03
	def parse_arguments(self):
		response = self.commands.parseArguments()
		return response
		
	# check to see, which arguments are passed in and do stuff according to the arguments
	def do_stuff(self):
		# if the response is not false
		if (not self.response == False): 
			for i in self.response[1].iterkeys():
				# if the file argument is passed, open the file and print the content
				# -f ex/ex.txt
				if (i == self.file): 
					with open(self.response[1][self.file],'r') as f:
						content = f.read()
						print ("Content of the file:-\n{0}".format(content))
				# if -h is passed as an argument, display help
				if (i == self.help): 
					self.commands.showHelp()
		else:
			print ("warning: NO ARGUMENTS passed")

	def __del__(self):
		return True
		
def main():
	example = Example()
	example.do_stuff()
		
if __name__ == "__main__":
	main()




