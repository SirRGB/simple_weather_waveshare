import configparser


def read_config():
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('config.ini')

    return config

def get_latitude():
    return read_config().getfloat('Weather', 'latitude')

def get_longitude():
    return read_config().getfloat('Weather', 'longitude')