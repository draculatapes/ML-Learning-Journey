import logging

# configure logging *before* using it
logging.basicConfig(
    filename="app.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    force=True   # <-- forces reconfiguration
)

def add(a, b):
    logging.debug("The addition operation is taking place")
    return a + b

logging.debug("The addition function is called")
print(add(10, 12))
