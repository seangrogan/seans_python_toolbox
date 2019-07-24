import os


def test_directory(path):
    """ Tests a file path and ensures the path exists.  If it does not exist, I will create the path
    :param path: String of a path
    """
    p = os.path.dirname(os.path.abspath(path))
    if not os.path.exists(p):
        os.makedirs(p)
