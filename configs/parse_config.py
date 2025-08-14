import configparser
from configparser import ConfigParser


def read_config() -> ConfigParser:
    # Create a ConfigParser object
    config = configparser.ConfigParser()

    # Read the configuration file
    config.read('configs/config.ini')

    return config

def get_full_refresh() -> str:
    return f"{config_file.getint('Display', 'full_refresh')}"

def get_display_target() -> str:
    return f"{config_file.get('Display', 'display_target')}"

def get_latitude() -> str:
    return f"{config_file.getfloat('Weather', 'latitude')}"

def get_longitude() -> str:
    return f"{config_file.getfloat('Weather', 'longitude')}"

def get_timezone() -> str:
    return f"{config_file.get('Weather', 'timezone')}"

config_file = read_config()