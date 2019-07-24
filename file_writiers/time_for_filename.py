import time


def time_for_filename(*, now=False, t_start=time.strftime("%Y%m%d_%H%M%S")):
    """ Gets a time string for the file names.
    :param now: if explicitly true, gets time at actual
    :param t_start: default argument, generates timestamp at project execution
    :return: string of time for filenames
    """
    return time.strftime("%Y%m%d_%H%M%S") if now else t_start