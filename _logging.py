import logging
logging.basicConfig(
  filename="app.log", # file name to store
  filemode="a",
  level=logging.INFO, # log level
  format="%(asctime)s - %(levelname)s - %(message)s"
  )


logging.info("user get logged in")
logging.warning("Warning generated")
logging.error("Error occurred")

print(1)

#creating a logger object
logger=logging.getLogger(__name__)
# __name__ gives module name

logger.setLevel(logging.DEBUG)
# logger will accept debug and above

file_handler=logging.FileHandler("app.log")
# this decides where logs will go on

file_handler.setLevel(logging.INFO)
# file will store INFO and above

formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

# how logs look like

file_handler.setFormatter(formatter)
# Attach format to handler

logger.addHandler(file_handler)
# Attach handler to logger

logger.info("Application started")
logger.error("An error occurred")