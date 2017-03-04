"""
Basic Open Street Map operations

geopandas might be a pain...
see http://geoffboeing.com/2014/09/using-geopandas-windows/

to set variables in a conda session:
https://conda.io/docs/using/envs.html#saved-environment-variables

set PATH=%PATH%C:/<path/to/omgeo>

"""

import osmnx as ox
city = ox.gdf_from_place('Newport, RI')
ox.plot_shape(ox.project_gdf(city))

G = ox.graph_from_address('43 Broadway, Newport, RI', network_type='drive')
ox.plot_graph(G)
