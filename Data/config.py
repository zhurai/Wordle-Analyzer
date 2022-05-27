# Python 3.10.4
import configparser
import sys
import pathlib
import argparse

# variables
configfile='DataConfig.ini'
config = configparser.ConfigParser()

try:
	# try to read configuration file
	CURRENT_DIRECTORY=pathlib.Path(__file__).parent
	theconfig=CURRENT_DIRECTORY / configfile
	config.read_file(theconfig.open("r"))
except:
	# if configuration file is empty	
	print("DEBUG: Unable to read configuration file")
	sys.exit(1)

# commandline arguments
parser = argparse.ArgumentParser(prog='Wordle Analyser')
parser.add_argument('-t','--test',action='store',help='Test Data File',default="none",metavar='TEST.txt',required=False)
args=parser.parse_args()

# debug message function
def debug(errortext):
	if config.has_option("GETDATA","debug"):
		if config.get('GETDATA','debug')=='1':
			print("DEBUG: " + errortext)
