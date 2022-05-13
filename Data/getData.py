# Python 3.10.4

import config
from git import Repo


def cloneGitRepository(source,destination):
	# check if "source" looks like a git repository
	# if it is not, send to the other function

	# if it is
	Repo.clone_from(source,destination)


# main function
def main():

	# clone the git repository
	configsource=config.config['GETDATA']['source']
	configdest=config.config['GETDATA']['destination']
	cloneGitRepository(configsource,configdest)

# check for proper environment to run main() function automatically
if __name__ == '__main__':
	main()

