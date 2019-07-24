import logging

import shapefile


def generic_esri_reader(shape_file, encoding='ISO-8859-1'):
    """Reads and parses the shape file into a more usable format"""
    print(f'Reading file {shape_file}')
    logging.debug(f'Opened File: {shape_file}')
    file = []
    with shapefile.Reader(shape_file, encoding=encoding) as sf:
        shapes, fields, records = sf.shapes(), sf.fields, sf.records()
        heading = [h.lower() for h in list(zip(*fields)).pop(0)[1:]] # Note 1
        for record, shape in zip(records, shapes):
            item = dict(zip(heading, list(record)))
            item['shape'] = shape
            file.append(item)
    return file

# Note 1 :
# this takes the field names and just pushes out the header. [1:] is included because I don't care about the deletion
# flag field. I'm also making sure that everything is lower case
