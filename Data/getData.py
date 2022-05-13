# Python 3.10.4
import config

# open file into memory, returns the data
def openFile(sourcefile):
	config.debug("Opening sourcefile: " + sourcefile) 
	with open(sourcefile,'r') as f:
		thefile=f.readlines()
	return thefile

# main function
def main():
	# open file into memory
	if config.config.has_option("GETDATA","source_file"):
		thefile=openFile("./english-words/"+config.config['GETDATA']['source_file'])
	else:
		config.debug("Unable to find 'source_file' entry in the configuration file")
		sys.exit(1)

# check for proper environment to run main() function automatically
if __name__ == '__main__':
	main()

