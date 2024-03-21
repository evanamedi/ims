import logging

def configure_logger():
    
    logger = logging.getLogger(__name__)
    
    logger.setLevel(logging.DEBUG)
    
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler('main.log')
    c_handler.setLevel(logging.WARNING)
    f_handler.setLevel(logging.DEBUG)
    
    c_format = logging.Formatter('%(filename)s | %(name)s | %(levelname)s | %(message)s')
    f_format = logging.Formatter('%(asctime)s | %(filename)s | %(name)s | %(levelname)s | %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)
    
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    
    return logger