# Python 3.10.4
import configparser


configfile='DataConfig.ini'
config = configparser.ConfigParser()

# try to read configuration file
config.read(configfile)

# if unable to read configuration file then output
