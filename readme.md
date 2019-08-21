# Sean's Python Toolbox

This repository is a set of tools that I am using across several projects.  I have them checked out to a location on my hard drive that is a member of `PYTHONPATH` and 

## File Readers

## File Writiers 

## Plotter

The `plotter` package is a package of items that assist in standardising plotting for my work.

Specifically `map_plotter.py` and the corresponding function `map_plotter()` is for plotting WGS/NAD (Lat/Lon) files using MatPlotLib

### WGS/NAD Map Plotter

The following are the argumemnts for the Map Plotter

`map_plotter(title, file=None, display=True, mp=True, **kwargs)`

Argument | Definintion 
--- | --- 
`title` | Title of the plot
`file` | Path and filename if you want to write the plot to a file.  Default is `None` if no file writing is desire
`display` | If `True` (default), plot is displayed.  Set to `False` if no display popup is reqired
`mp` | If `True` (default), a new process is spawned and the plotting of the figure is sent to this new process.  Useful for large or complex drawings.  `False` will let the current process writie the plot.  

Keyword Arguments | Definiton
--- | --- 
`counties` | Plots a list of shapes that are representative of county juristictions
`stations` | Plots a scatterplot of fire stations
`roads` | Plots roads
`lsrs` | Plots local storm reports, currently only tornadoes 
`sbws` | Plots storm based warnings
`solution` or `tours` | a dict of list of points, i.e. the tour.  
`points` | Simply plots a scatterplot of the points in green
`waypoints` | Simply plots a scatterplot of the waypoints in blue
`bbox` | Bounding box in a `tuple`/`list` of length of 4 in the format of `[left, bottom, right, top]` or dict with keys of the same names.  None keeps the bounds automatic.  A list with length less than 4 will apply none to the last keys.   
`scale` | `True` (default) will plot a scalebar, `False` will leave it empty
`location` | the location of the scalebar, default is `lower left`, but it can take some combination of `upper, lower, center, left, right`


## Tools

The `tools` package includes the `try_to_number(value)` file which takes `value` and attempts to incorporate it into a float or int (if applicable)

# Index

Function Name | Location |  Notes
--- | --- | ---
`generic_csv_reader(csv_file, encoding)` | file_readers/generic_csv.py | Reads a CSV file with Geospatial data and returns the file with a a 'fake shape opbject' to ensure compatibility with ESRI Shape Files
`generic_esri_reader(shape_file, encoding)` | file_readers/generic_ersi.py | Reads a shape file and returns a list of features
`generic_geospatial(file, encoding)` | file_readers/generic_geospatial.py | Allows passing of a SHP/DBF file or a CSV file to be read
`generic_geospatial_files(file_iterable, encoding)` | file_readers/generic_geospatial.py | Allows passing of a `list` or `set` of SHP/DBF files or a CSV files to be read.  Can be mixed types
`map_plotter(title, file=None, display=True, mp=True, **kwargs)` | plotter/map_plotter.py | plotting WGS/NAD (Lat/Lon) data
`shp_or_csv(file)`, `is_csv(file)`, `is_shp(file)` |file_readers/shp_or_csv.py| Tests the extensions of the files passesd into `generic_geospatial()`
`test_directory(path)` | file_writiers/test_directory.py | Tests a file path and ensures the path exists.  If it does not exist, I will create the path
`time_for_filename()` | file_writiers/time_for_filename.py | Gets a time string for the file names.
`try_to_number(value)` | tools/try_to_number.py | Tries to make `value` into a float or int\
