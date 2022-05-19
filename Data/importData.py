# Python 3.10.4
import config
import sys
import getData

def saveFile(TheData,TargetFile):
    # TheData = list of words
    # TargetFile = where to save into

    # Erase previous contents of the file
    config.debug("Erasing contents of file: " + TargetFile)
    file = open(TargetFile,"w+")
    file.truncate(0)
    file.close()

    # Save new data into the file
    config.debug("Updating contents of file: " + TargetFile)
    with open(TargetFile,'w+') as f:
        for line in TheData:
            f.write(line+"\n")

# main function
def main():
    pass

# check for proper environment to run main() function automatically
if __name__ == '__main__':
	main()
