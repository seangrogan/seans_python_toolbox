import logging
from multiprocessing import Process

import matplotlib.pyplot as plt
from file_writiers.test_directory import test_directory
from great_circle_calculator import great_circle_calculator as gcc
from matplotlib_scalebar.scalebar import ScaleBar

_z_orders = {
    "grid": 0,
    "counties": 10,
    "fire_stations": 25,
    "roads": 15,
    "lsrs": 50,
    "sbws": 20,
    "points": 30,
    "waypints": 40
}


def map_plotter(title, file=None, display=True, mp=True, **kwargs):
    if mp:
        p_args = (title, file, display)
        Process(target=_map_plotter, args=p_args, kwargs=kwargs).start()
    else:
        _map_plotter(title, file, display, **kwargs)


def _map_plotter(title, file=None, display=True, **kwargs):
    fig, ax = plt.subplots()
    info = f"Plotting {title}" if file is None else f"Plotting {title} to {file}"
    print(info)
    logging.debug(info)
    _setup(ax, fig, title, dpi_override=kwargs.get("dpi", None))
    if kwargs.get("counties", None) is not None:
        _plot_counties(ax, kwargs.get("counties", None))
    if kwargs.get("stations", None) is not None:
        _plot_fire_stations(ax, kwargs.get("stations", None),
                            plot_with_label=kwargs.get("stations_labels", False))
    if kwargs.get("roads", None) is not None:
        _plot_roads(ax, kwargs.get("roads", None))
    if kwargs.get('lsrs', None) is not None:
        _plot_lsrs(ax, kwargs.get('lsrs', None))
    if kwargs.get('sbws', None) is not None:
        _plot_sbws(ax, kwargs.get('sbws', None))
    if kwargs.get("points", None) is not None:
        _plot_points(ax, fig, kwargs.get("points", None))
    if kwargs.get("waypoints", None) is not None:
        _plot_waypoints(ax, kwargs.get("waypoints", None))
    if kwargs.get("scale", True):
        _plot_scale(ax, fig, **kwargs)
    if file is not None:
        test_directory(file)
        fig.savefig(file.replace(" ", "_"), bbox_inches=kwargs.get("bbox_inches", "tight"))
    if display:
        plt.show()
    plt.close(fig=fig)


def _plot_waypoints(ax, waypoints):
    x, y = zip(*waypoints)
    ax.scatter(x, y, color="blue", marker='.', zorder=_z_orders.get("waypoints", None))
    pass


def _plot_points(ax, fig, points):
    x, y = zip(*points)
    ax.scatter(x, y, color="green", marker='.', zorder=_z_orders.get("points", None))


def _plot_lsrs(ax, lsrs):
    for lsr in lsrs:
        x, y = lsr['lon'], lsr['lat']
        ax.scatter(x, y, c="red", marker="$T$", zorder=_z_orders.get("lsrs", None))



def _plot_sbws(ax, sbws):
    for sbw in sbws:
        if sbw["phenom"] == "TO":
            color, line = "red", '--'
        else:
            color, line = "yellow", '-.'
        x, y = zip(*sbw["shape"].points)
        ax.plot(x, y, color=color, linestyle=line, linewidth=0.5, zorder=_z_orders.get("sbws", None))


def _plot_roads(ax, roads):
    for road in roads:
        x, y = zip(*road)
        ax.plot(x, y, color="blue", linestyle="-", linewidth=0.25, zorder=_z_orders.get("roads", None))


def _plot_fire_stations(ax, fire_stations, plot_with_label=False):
    items = fire_stations
    if isinstance(fire_stations, dict):
        keys, items = zip(*fire_stations.items())
    for station in items:
        x, y = station["x"], station["y"]
        ax.scatter(x, y, color="red", marker="8", zorder=_z_orders.get("fire_stations", None), s=(1, 1))
        if plot_with_label:
            name_split = station["name"].split(" ")
            name = " ".join([item.capitalize() for item in name_split])
            ax.annotate(xy=(x, y), s=name, zorder=_z_orders.get("fire_stations", None) + 2,
                        ha="center", va="bottom", fontsize="xx-small")


def _plot_counties(ax, counties):
    items = counties
    if isinstance(counties, dict):
        keys, items = zip(*counties.items())
    for item in items:
        x, y = zip(*item["shape"].points)
        ax.plot(x, y, color="black", linestyle="-", linewidth=0.5, zorder=_z_orders.get("counties", None))


def _plot_scale(ax, fig, **kwargs):
    x1, x2, y1, y2 = ax.axis()
    _y = (y1 + y2) / 2
    p1, p2 = (int(x1), _y), (int(x1) + 1, _y)
    meter_per_deg = gcc.distance_between_points(p1, p2)
    scale_bar = ScaleBar(meter_per_deg, units="m", location=kwargs.get("location", "lower left"),
                         fixed_value=kwargs.get("fixed_value", None), fixed_units=kwargs.get("fixed_units", None))
    fig.gca().add_artist(scale_bar)


def _setup(ax, fig, title, dpi_override=None, x_lab="Longitude", y_lab="Latitude"):
    fig.gca().set_aspect("equal", adjustable="box")
    ax.grid(zorder=_z_orders.get("grid", None))
    ax.set_title(label=title)
    if dpi_override is not None:
        fig.dpi = dpi_override
    ax.set_xlabel(x_lab)
    ax.set_ylabel(y_lab)
