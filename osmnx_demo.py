"""
Basic Open Street Map operations

geopandas might be a pain...
see http://geoffboeing.com/2014/09/using-geopandas-windows/

This is just messing around with some of the demo scripts on http://geoffboeing.com/2016/11/osmnx-python-street-networks/

"""

import osmnx as ox
import networkx as nx
import pandas as pd

city = ox.gdf_from_place('Newport, RI')
ox.plot_shape(ox.project_gdf(city))

walk_graph = ox.graph_from_address('Broadway, Newport, RI', network_type='walk')
ox.plot_graph(walk_graph)

newport_streets = ox.graph_from_place('Newport, RI')
ox.plot_graph(newport_streets)

# do some analysis
basic_stats = ox.basic_stats(newport_streets)
# the extended stats can take a while, so comment out by default to avoid taking too much time
# extended_stats = ox.extended_stats(H, bc=True)

# print(extended_stats['betweenness_centrality_avg'])

# plot graph with edges colored by length
edge_length_colors = ox.get_edge_colors_by_attr(newport_streets, attr='length')
ox.plot_graph(newport_streets, edge_color=edge_length_colors)

# plot graph with one-way streets in red
one_way_colors = ['r' if data['oneway'] else 'b' for u, v, key, data in newport_streets.edges(keys=True, data=True)]
ox.plot_graph(newport_streets, node_size=0, edge_color=one_way_colors)

# routes. location is from the tutorial.  adjust location_point, origin_point, and destination_point.
location_point = (37.791427, -122.410018)
route_demo_network = ox.graph_from_point(location_point, distance=500, distance_type='network', network_type='walk')
G_proj = ox.project_graph(route_demo_network)
origin_point = (37.792896, -122.412325)
destination_point = (37.790495, -122.408353)
origin_node = ox.get_nearest_node(route_demo_network, origin_point)
destination_node = ox.get_nearest_node(route_demo_network, destination_point)
# use networkx to calculate the shortest path
route = nx.shortest_path(route_demo_network, origin_node, destination_node, weight='length')
ox.plot_graph_route(route_demo_network, route, origin_point=origin_point, destination_point=destination_point)

# Accessing street data
# use pandas to turn the network into a dataframe and work with street attributes
sf = pd.DataFrame(newport_streets.edges(data=True))  # intermediate variable
street_frame = pd.concat([sf.drop(2,axis=1),sf[2].apply(pd.Series)],axis=1)
