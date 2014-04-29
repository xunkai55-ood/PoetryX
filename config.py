class DefaultConfig(object):

    def __init__(self):

        host_conf = 0

        if host_conf == 0:
            self.MONGO_HOST = "localhost"
            self.MONGO_PORT = 27017

default_config = DefaultConfig()
