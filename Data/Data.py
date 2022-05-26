# Python 3.10.4
import config
import getData
import sys
import importData
import pathlib

# main function
def main():
	# open file into memory
	if config.config.has_option("GETDATA","source_file"):
		try:
			sourcedata,sourcelength=getData.openFile(config.CURRENT_DIRECTORY / "english-words" / config.config.get('GETDATA','source_file'))
		except:
			config.debug("Unable to use data from " + str(config.CURRENT_DIRECTORY / "english-words" / config.config.get('GETDATA','source_file')))
			sys.exit(1)
	else:
		config.debug("Unable to find 'source_file' entry in the configuration file, attempting to use test_data.txt")
		try: 
			sourcedata,sourcelength=getData.openFile(config.CURRENT_DIRECTORY / "test_data.txt")
		except:
			config.debug("Unable to use data from " + str(config.CURRENT_DIRECTORY / "test_data.txt"))
			sys.exit(1)

	# filter the list for words that are word_length long
	if config.config.has_option("GETDATA","word_length"):
		wordlength=int(config.config['GETDATA']['word_length'])
		editeddata,editedlength=getData.filterData(sourcedata,wordlength)
	else:
		config.debug("Unable to find 'word_length' entry in the configuration file")
		sys.exit(1)

	# save the edited data into a new file
	if config.config.has_option("IMPORTDATA","target_text_file"):
		targetfile=importData.getOutputPath() / config.config['IMPORTDATA']['target_text_file']
		importData.saveWordsFile(editeddata,targetfile)
	else:
		config.debug("Unable to find 'target_file' entry in the configuration file")
		sys.exit(1)
	
    # get statistics about the data
	sourcestats=getData.getInformation(sourcedata,sourcelength,False)
	editedstats=getData.getInformation(editeddata,editedlength,True)

	# output statistics about the data
	print("Source File Statistics")
	for x in sourcestats:
		print(" " + x + " " + str(sourcestats[x]))
	print("\n")
	print("Edited File Statistics")
	for x in editedstats:
		print(" " + x + " " + str(editedstats[x]))
	
	# save the statistics data into a new file
	if config.config.has_option("IMPORTDATA","target_stats_original_file"):
		targetfile=importData.getOutputPath() / config.config['IMPORTDATA']['target_stats_original_file']
		importData.saveWordsFile(sourcestats,targetfile)
	else:
		config.debug("Unable to find 'target_stats_original_file' entry in the configuration file")
		sys.exit(1)
	
	if config.config.has_option("IMPORTDATA","target_stats_edited_file"):
		targetfile=importData.getOutputPath() / config.config['IMPORTDATA']['target_stats_edited_file']
		importData.saveWordsFile(editedstats,targetfile)
	else:
		config.debug("Unable to find 'target_stats_edited_file' entry in the configuration file")
		sys.exit(1)

# check for proper environment to run main() function automatically
if __name__ == '__main__':
	main()

