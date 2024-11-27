import logging

# 1. root logger
# 1-1. configure logging to print to the console with a specific format and log level
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 1-2. Write the log to the file
logging.basicConfig(
    filename='example.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

# Now, you can log messages at different severity levels
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is an critical message')


# 2. Custom logger
# 2-1. Create a custom logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG) # Set the log level to DEBUG to capture all types of messages

# 2-2. Create a file handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
# File handler
file_handler = logging.FileHandler('my_app.log')
file_handler.setLevel(logging.DEBUG)

file_handler.setFormatter(formatter)

# Stream handler
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.DEBUG)

stream_handler.setFormatter(formatter)


# GCP Logging
from google.cloud import logging as gcp_logging

client = gcp_logging.Client(project='tpcg-ygpark-temp')
client.setup_logging() # 코드가 실행되는 환경에 가장 적합한 구성을 선택, log_level=logging.INFO


# 2-3. Add the file handler to the logger
# logger.addHandler(file_handler)
logger.addHandler(stream_handler)

# Now, you can log messages at different severity levels
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is an critical message')




