import logging

logger = logging.getLogger("my_logger")

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.WARNING)
f_handler = logging.FileHandler("file.log")
f_handler.setLevel(logging.ERROR)

c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

logger.addHandler(c_handler)
logger.addHandler(f_handler)

logger.warning("First warning!")
logger.error("Some error")
logger.debug("Some debugging")
logger.warning("Second warning!")
logger.critical("Critical situation!")
