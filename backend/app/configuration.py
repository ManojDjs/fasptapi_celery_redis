import os
import configparser
from configparser import ExtendedInterpolation

# Set default environment variables if not present
os.environ.setdefault('LOG_LEVEL', 'INFO')

# Set up logging
# Load configuration
config = configparser.ConfigParser(os.environ,interpolation=ExtendedInterpolation())
config.read('config.ini')