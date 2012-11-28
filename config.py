#!/usr/bin/env python3
"""
This is the config part of VocVoc.
"""


import configparser
from os.path import dirname, join as pJoin


__config__ = 'config.ini'
__dir__ = dirname(__file__)
#__path__ = join(__dir__, __config__)
__config__ = pJoin(__dir__, __config__)


class Config :
    """
    This is the class which stores the configs.
    """

    def __init__(self) :
        self.config = configparser.ConfigParser()
        self.config.read(__config__)
        self.getConfig()

    def getConfig(self) :
        config = self.config
        self.corpusDir = config['Path']['corpusDir']
        self.pickleDir = config['Path']['pickleDir']

    def setConfig(self, section, option, value) :
        try :
            self.config[section][option] = value
            with open(__config__, 'w') as configFile :
                self.config.write(configFile)
        except TypeError as error :
            pass


if __name__ == '__main__':

    config = Config()
    #config.setConfig('Path', 'corpusDir', '')
