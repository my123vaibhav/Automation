import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('Utilities/properties.ini')
    return config


def getPassword():
    return "Srinath19830G"
