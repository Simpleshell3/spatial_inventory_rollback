import datetime
import logging

# exclude numba
numba_logger = logging.getLogger("numba")
numba_logger.setLevel(logging.WARNING)


def start_logging(level):
    rootLogger = logging.getLogger()

    logFormatter = logging.Formatter(
        "%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
    )

    log_path = "spatial_rollback_{date}.log".format(
        date=datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    )
    fileHandler = logging.FileHandler(log_path, "w")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

    rootLogger.setLevel(level)


def get_logger():
    return logging.getLogger("spatial_rollback")
