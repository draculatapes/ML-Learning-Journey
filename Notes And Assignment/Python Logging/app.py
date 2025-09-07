import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
        logging.FileHandler('app1.log'),
        logging.StreamHandler()
    ]
)
logger=logging.getLogger('ArithmaticApp')

def add(a,b):
    result=a+b
    logger.debug(f'adding {a} and {b} : {result} ' )
    return result
def mul(a,b):
    result=a*b
    logger.debug(f'mul {a} and {b} : , {result} ')
    return result
def sub(a,b):
    result=a-b
    logger.debug(f'sub {a} and {b} : , {result}')
    return result
def div(a,b):
    try:
        result=a/b
        logger.debug(f" diviing {a} and {b} , {result}")
    except ZeroDivisionError:
        logger.error('division by zero error')

add(1,2)
mul(2,3)
sub(3,2)
div(1,2)
div(3,0)
