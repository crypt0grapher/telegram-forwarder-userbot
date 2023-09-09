import logging


def safe_int_parse(text):
    try:
        return int(text)
    except ValueError:
        logging.debug(f"Could not parse '{text}' as an integer.")
        return None


def safe_float_parse(text):
    try:
        return float(text)
    except ValueError:
        logging.debug(f"Could not parse '{text}' as an float.")
        return None
