# Python 3.10.4
import configparser
import sys

# variables
configfile='DataConfig.ini'
config = configparser.ConfigParser()

try:
	# try to read configuration file
	config.read_file(open("DataConfig.ini","r"))
except:
	# if configuration file is empty	
	print("DEBUG: Unable to read configuration file")
	sys.exit(1)