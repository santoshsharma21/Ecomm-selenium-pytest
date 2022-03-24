# import lib
import logging


class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="./logs/automation.log", level=logging.INFO, force=True,
                            format="%(asctime)s: %(levelname)s: %(message)s",
                            datefmt="%d-%b-%Y %H:%M:%S")
        logger = logging.getLogger()
        # logger.setLevel(logging.INFO)
        return logger
