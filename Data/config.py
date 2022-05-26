# Python 3.10.4
import configparser
import sys
import pathlib

# variables
configfile='DataConfig.ini'
config = configparser.ConfigParser()

try:
	# try to read configuration file
	thepath=pathlib.Path(__file__).parent
	theconfig=thepath / configfile
	config.read_file(theconfig.open("r"))
except:
	# if configuration file is empty	
	print("DEBUG: Unable to read configuration file")
	sys.exit(1)

# debug message function
def debug(errortext):
	if config.has_option("GETDATA","debug"):
		if config.get('GETDATA','debug')=='1':
			print("DEBUG: " + errortext)
