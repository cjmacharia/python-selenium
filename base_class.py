import logging


class TestLogger:
    def test_logging(self):
        print('got here safe cj')
        logger = logging.getLogger(__name__)
        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        fileHandler.setFormatter(formatter)
        logger.addHandler(fileHandler)
        logger.setLevel(logging.INFO)
        return logger


logger = TestLogger()
