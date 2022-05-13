# Python 3.10.4

import config
import getData

# main function
def main():

	# clone the git repository
	configsource=config.config['GETDATA']['source']
	configdest=config.config['GETDATA']['destination']
	getData.cloneGitRepository(configsource,configdest)

# check for proper environment to run main() function automatically
if __name__ == '__main__':
	main()

