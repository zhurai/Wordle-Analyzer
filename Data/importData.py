# Python 3.10.4
import config
import pathlib
import csv

def getOutputPath():
    thepath=pathlib.Path(__file__).parent / 'output'
    
    # if the output directory does not exist, create it
    if thepath.exists() is False:
        pathlib.Path.mkdir(thepath)
    
    # returns an pathlib.Path object
    return thepath

def saveStatsFile(thedata,thefile):
    # thedata = list of words
    # thefile = where to save into (pathlib.Path)

    # Erase previous contents of the file
    config.debug("Erasing contents of file: " + str(thefile))
    file = thefile.open("w")
    file.truncate(0)
    file.close()

    # Save new data into the file
    config.debug("Updating contents of file: " + str(thefile))
    with thefile.open('w',newline='') as file:
        filewriter=csv.writer(file)
        for header in thedata:
            filewriter.writerow([header,str(thedata[header])])


def saveWordsFile(thedata,thefile):
    # thedata = list of words
    # thefile = where to save into (pathlib.Path)

    # Erase previous contents of the file
    config.debug("Erasing contents of file: " + str(thefile))
    file = thefile.open("w")
    file.truncate(0)
    file.close()

    # Save new data into the file
    config.debug("Updating contents of file: " + str(thefile))
    with thefile.open('w') as file:
        for line in thedata:
            file.write(line+"\n")
