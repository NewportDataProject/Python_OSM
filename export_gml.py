"""
exporting newport's street graph to a GML file.
"""

import osmnx as ox
import networkx as nx
import shapely.wkt

streetgraph = ox.graph_from_place('Newport, RI')


def prepForWriting(streetgraph):

    ## pull out this graph attribute, and put it into each node
    for node in streetgraph.graph['streets_per_node']:
        streetgraph.node[node]['numstreets'] = streetgraph.graph['streets_per_node'][node]
    del streetgraph.graph['streets_per_node']

    ## GML serializer can't handle shapely linestrings, so convert them
    for node1 in streetgraph.edge:
        for node2 in streetgraph.edge[node1]:
            for ix in streetgraph.edge[node1][node2]:
                if 'geometry' in streetgraph.edge[node1][node2][ix]:
                    streetgraph.edge[node1][node2][ix]['geostr'] = shapely.wkt.dumps(streetgraph.edge[node1][node2][ix]['geometry'])
                    del streetgraph.edge[node1][node2][ix]['geometry']

prepForWriting(streetgraph)

nx.write_gml(streetgraph, "newport_streets.gml")
