import logging
import os


class LoggerUtilities:
    def __init__(self, log_file='Logs/app.log'):
        self.log_file = log_file
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        logging.basicConfig(filename=log_file, level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
        self.logger = logging.getLogger()

    def get_logger(self):
        return self.logger


if __name__ == '__main__':
    logger = LoggerUtilities().get_logger()
    logger.info('****** This is an info log message ******')