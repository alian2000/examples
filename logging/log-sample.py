
import logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.
# Python has six log levels with each one assigned a specific integer indicating the severity of the log:

# NOTSET=0
# DEBUG=10
# INFO=20
# WARN=30
# ERROR=40
# CRITICAL=50

logging.basicConfig(filename='test.log', level=logging.CRITICAL,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 20
num_2 = 10
constant=99





sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

add_result_with_constant = add(num_1, constant)
logging.info('Add: {} + {} = {}'.format(num_1,constant , add_result_with_constant))

add_result = add(num_1, num_2)
logging.warning('Add: {} + {} = {}'.format(num_1, num_2, add_result))

mul_result = multiply(num_1, num_2)
logging.error('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.critical('Div: {} / {} = {}'.format(num_1, num_2, div_result))
