import logging

logging.basicConfig(filename='my.log', filemode='w',
                    format='%(name)s - %(levelname)s - %(message)s - '
                           '%(process)d - %(asctime)s',
                    datefmt='%d-%b-%y %H:%M:%S')
logging.warning('First message in log file')
logging.error('Second message')

name = 'MyLogger'
logging.error('%s caused error', name)

try:
    c = 5 / 0
except ArithmeticError as e:
    logging.error("Division by zero", exc_info=False)
    logging.exception("Zero division occurred!")
