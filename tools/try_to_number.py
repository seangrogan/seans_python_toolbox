def try_to_number(value: str):
    """ Takes value string and tries to convert it into
    :param value: str that is a line or element of a file
    :return: either the value as a string, int, or float.  Whatever best fits.
    """
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            try:
                return float(value)
            except ValueError:
                return value
    raise ValueError(f"Could not parse {value}")
