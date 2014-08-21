import os
import yaml


def load_settings(settings):
    '''
    Load settings.yaml
    This file contain:
        - variables for templates
        - packages for installation
        - sources and destination folders
        - etc
    '''
    settings_file = settings

    # Modules settings
    #ROOT_DIR = os.path.abspath(os.path.dirname(__file__))
    ROOT_DIR = os.getcwd()
    SETTINGS_DIR = os.path.join(ROOT_DIR, 'settings')
    SETTINGS_DATA = os.path.join(SETTINGS_DIR, settings_file)

    try:
        with open(SETTINGS_DATA) as stream:
            data = yaml.load(stream)
            return data
    except IOError as error:
        print ('File error: ' + str(error))
