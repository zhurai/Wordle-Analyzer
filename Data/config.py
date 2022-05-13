# Python 3.10.4
import configparser
import sys

# variables
configfile='DataConfig.ini'
config = configparser.ConfigParser()

try:
	# try to read configuration file
	config.read_file(open(configfile,"r"))
except:
	# if configuration file is empty	
	print("DEBUG: Unable to read configuration file")
	sys.exit(1)

# debug message function
def debug(errortext):
	if config.config.has_option("GETDATA","debug"):
		if config['GETDATA']['debug']=='1':
			print("DEBUG: " + errortext)
	else: 
		# unable to find debug entry in configuration file, just ignoring
