from file_readers.generic_csv import generic_csv_reader
from file_readers.generic_ersi import generic_esri_reader
from file_readers.shp_or_csv import is_shp, is_csv


def generic_geospatial(file, encoding='ISO-8859-1'):
    if is_shp(file):
        return generic_esri_reader(file, encoding)
    elif is_csv(file):
        return generic_csv_reader(file, encoding)


def generic_geospatial_files(file_iterable, encoding='ISO-8859-1'):
    if isinstance(file_iterable, set) or isinstance(file_iterable, list):
        files = []
        for file in file_iterable:
            files.append(generic_geospatial(file, encoding))
        if len(files) == 1:
            return files[0]
        return files
    return generic_geospatial(file_iterable)
