API_VERSION = "0.0.1"

class ConfigClass(object):
    DEBUG = False
    TESTING = False
    API_NAME = "my_app"

class DevClass(ConfigClass):
    DEBUG = True

class TestingClass(ConfigClass):
    TESTING = True
