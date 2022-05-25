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
		sourcedata,sourcelength=getData.openFile(str(pathlib.Path(__file__).parent)+"\english-words\\"+config.config.get('GETDATA','source_file'))
	else:
		config.debug("Unable to find 'source_file' entry in the configuration file, attempting to use test_data.txt")
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
		targetfile=str(pathlib.Path(__file__).parent)+"\\"+config.config['IMPORTDATA']['target_text_file']
		importData.saveFile(editeddata,targetfile)
	else:
		config.debug("Unable to find 'target_file' entry in the configuration file")
		sys.exit(1)
	
    # get statistics about the data
	sourcestats=getData.getInformation(sourcedata,sourcelength,False)
	editedstats=getData.getInformation(editeddata,editedlength,True)

	# output statistics about the data
	#print("Source File Statistics")
	#for x in sourcestats:
	#	print(" " + x + " " + str(sourcestats[x]))
	#print("\n")
	#print("Edited File Statistics")
	#for x in editedstats:
	#	print(" " + x + " " + str(editedstats[x]))

# check for proper environment to run main() function automatically
if __name__ == '__main__':
	main()

