import logging

def configure_logger(name, log_to_console=False):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    fh = logging.FileHandler("app.log")
    fh.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler()
    if log_to_console:
        ch.setLevel(logging.ERROR)
    else:
        ch.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger