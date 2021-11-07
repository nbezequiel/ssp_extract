import logging

class Logger:
    def __init__(self):
        FORMAT = "[%(levelname)s %(asctime)-15s %(module)s:%(lineno)s - %(funcName)10s() ] %(message)s"
        logging.basicConfig(format=FORMAT)
        logging.basicConfig(level=logging.INFO)
        self.log = logging.getLogger(self.__class__.__name__)
        self.log.setLevel(logging.DEBUG)