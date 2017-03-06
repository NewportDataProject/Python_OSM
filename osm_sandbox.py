from osmapi import OsmApi
import overpy

# Using osmapi
# Create the API instance
MyApi = OsmApi()

# Get the data for a node at the Viking intersection
my_node = MyApi.NodeGet(201125350)
print(my_node)
#{'id': 201125350, 'lon': -71.3096479, 'version': 3, 'user': 'maxerickson', 'timestamp': datetime.datetime(2014, 10, 20, 0, 57, 42), 'lat': 41.4878232, 'tag': {}, 'changeset': 26204331, 'visible': True, 'uid': 360392}

# Get the data for Broadway
my_street = MyApi.WayGet(19356382)
# print just the tags, not the nodes that make it up
print(my_street.get('tag'))
#{'highway': 'secondary', 'surface': 'asphalt', 'name': 'Broadway', 'sidewalk': 'both', 'maxspeed': '25 mph', 'lit': 'yes', 'lanes': '2'}


#Using Overpy example
api = overpy.Overpass()

result = api.query("""
    way(50.746,7.154,50.748,7.157) ["highway"];
    (._;>;);
    out body;
    """)

for way in result.ways:
    print("Name: %s" % way.tags.get("name", "n/a"))
    print("  Highway: %s" % way.tags.get("highway", "n/a"))
    print("  Nodes:")
    for node in way.nodes:
        print("    Lat: %f, Lon: %f" % (node.lat, node.lon))

