import configparser
from configparser import ConfigParser


def read_config() -> ConfigParser:
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('config.ini')

    return config

def get_latitude() -> str:
    return f"{read_config().getfloat('Weather', 'latitude')}"

def get_longitude() -> str:
    return f"{read_config().getfloat('Weather', 'longitude')}"

def get_full_refresh() -> str:
    return f"{read_config().getint('Display', 'full_refresh')}"

def get_timezone() -> str:
    return f"{read_config().get('Weather', 'timezone')}"
