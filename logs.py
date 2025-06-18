# import logging

# logging.basicConfig(
#     filename="logs.log",
#     level=logging.DEBUG,
#     filemode="w",)
# logging.info("The script is about to start.")
# def division(a: float, b: float) -> float:
#     """Returns the division of two numbers."""
#     logging.debug(f"Dividing {a} by{b}.")
#     result: float= a/b
#     logging.debug(f"Result:{result}.")
#     return result
# result= division(10,2)
# logging.info( "the script has finished")


import logging

logging.basicConfig(
    filename="logs.log",
    level=logging.DEBUG,
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",)
logging.info("The script is about to start.")
def division(a: float, b: float) -> float:
    """Returns the division of two numbers."""
    logging.debug(f"Dividing {a} by{b}.")
    result: float = 0.0
    try:
        result: float= a/b
    except ZeroDivisionError as e:
        logging.error(f"Error occurred:{e}.")
        logging.warning(f"Division by zero is not allowed")
    logging.debug(f"Result:{result}.")
    return result
result= division(8,2)
logging.info( "the script has finished")