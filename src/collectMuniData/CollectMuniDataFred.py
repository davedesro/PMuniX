# -----------------------------------------------------------------------------
#
#   CollectMuniData.py
#   By: Fred Stakem
#   Date: 10.23.11
#
#   Purpose: This file will connect to the Muni server and download data 
#            so we some data to play with.
#
# -----------------------------------------------------------------------------

# Documentation
# -------------
# Types of requests
# 1) Configuration request
# 2) Prediction request
# 3) Location request
# 4) Arrival/Departure request
#
# Example
#   http://webservices.nextbus.com/service/publicXMLFeed?command=commandName&a=sf-muni&additionParams...
#
# Commands [http://www.sfmta.com/cms/asite/nextmunidata.htm]
# 1) "routeList" --> basic route names list
# 2) "routeConfig" --> given route name, return all associated stops w/ IDs and geo location
# 3) "predictions" --> given stop #, determine in/outbound buses
# 4) "predictionsForMultiStops"
# 5) "vehicleLocations"  --> return geo coordinates of buses, per <route> and <time> (only changes returned)
# 
# Command Examples
# 1) Get all routes
#    http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni
# 2) Get specific route information (in example 'F' is the route tag)
#    http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni&r=F
# 3) Get vehicle locations (in example 'N' is the route tag and '1144953500233' is the ms time of the last sample)
#    http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&r=N&t=1144953500233

# Libraries
import pdb
import xml.etree.ElementTree as xmlparser
import urllib2
import time
import re
from xml.dom.minidom import parseString

# Constants
SF_MUNI_URL = 'http://webservices.nextbus.com/service/publicXMLFeed?command='

# Helper functions
def enum(**enums):
    return type('Enum', (), enums)
    
    # Example
    #Numbers = enum(ONE=1, TWO=2, THREE='three')
    #Numbers.ONE
    #1
    #Numbers.TWO
    #2

# Models   
class Parser(object):
    
    TITLE_LABEL = "title"
    TAG_LABEL = "tag"
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass
     
    @staticmethod   
    def get_data_from_dict(values):
        pass
            
class StopParser(Parser):
    
    ID_LABEL = "stopId"
    LATITUDE_LABEL = "lat"
    LONGITUDE_LABEL = "lon"
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
    
    @staticmethod    
    def get_data_from_dict(values):
        stop = Stop()
        stop.id = int( values.get(StopParser.ID_LABEL) )
        stop.name = values.get(Parser.TITLE_LABEL)
        stop.tag = values.get(Parser.TAG_LABEL)
        latitude = float( values.get(StopParser.LATITUDE_LABEL) )
        longitude = float( values.get(StopParser.LONGITUDE_LABEL) )
        location = Location(latitude, longitude)
        
        return stop
       
class DirectionParser(Parser):
    
    NAME_LABEL = "name"
    NAMES = ['Inbound', 'Outbound'] 
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
    
    @staticmethod    
    def get_data_from_dict(values):
        direction = Direction()
        if values.get(DirectionParser.NAME_LABEL) == DirectionParser.NAMES[0]:
            direction.type = Direction.INBOUND
        else:
            direction.type = Direction.OUTBOUND
        direction.name = values.get(Parser.TITLE_LABEL)
        direction.tag = values.get(Parser.TAG_LABEL)    
        
        return direction
             
class RouteParser(Parser):
    
    LATITUDE_MIN_LABEL = 'latMin'
    LATITUDE_MAX_LABEL = 'latMax'
    LONGITUDE_MIN_LABEL = 'lonMin'
    LONGITUDE_MAX_LABEL = 'lonMax'
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    @staticmethod
    def parse_route_from_xml(xml):
        root_xml = xmlparser.fromstring(xml)
        route_xml = list(root_xml)
        route = RouteParser.get_data_from_dict(route_xml[0].attrib)
        print str(route)

        # TODO -> follow a similar pattern below and find out why I have to make a list to get route_xml
        stops = root_xml.findall("route/stop")
        for stop in stops:
            pass
            #print "  ", stop.tag, stop.attrib

        directions = root_xml.findall("route/direction")
        for direction in directions:
            #print "  ", direction.tag, direction.attrib
            stops = direction.findall("stop")
            for stop in stops:
                pass
                #print "  ", "  ", stop.tag, stop.attrib

        paths = root_xml.findall("route/path")
        for path in paths:
            #print "  ", path.tag, path.attrib
            points = path.findall("point")
            for point in points:
                pass
                #print "  ", "  ", point.tag, point.attrib
    
    @staticmethod    
    def get_data_from_dict(values):
        route = Route()
        route.name = values.get(Parser.TITLE_LABEL)
        route.tag = values.get(Parser.TAG_LABEL)
        latitude_min = float( values.get(RouteParser.LATITUDE_MIN_LABEL) )
        latitude_max = float( values.get(RouteParser.LATITUDE_MAX_LABEL) )
        longitude_min = float( values.get(RouteParser.LONGITUDE_MIN_LABEL) )
        longtitude_max = float( values.get(RouteParser.LONGITUDE_MAX_LABEL) )
        route.bounding_box = [ [latitude_min, latitude_max], [longitude_min, longtitude_max] ]
        
        return route
        
class Location(object):

    def __init__(self, latitude=0.0, longitude=0.0):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '(' + str(self.latitude) + ', ' + str(self.longitude) + ')'
 
class Stop(object):
    
    def __init__(self, stop_id=-1, name="Generic Stop", tag=-1, location=Location()):
        self.id = stop_id
        self.name = name
        self.tag = tag
        self.location = location
        
    def __str__(self):
        return self.name + '(' + str(self.id) + ') Location: ' + str(self.location)
        
class Direction(object):
    
    DirectionType = enum(INBOUND=1, OUTBOUND=2)
    # Is there a way to do this in constructor: dir_type=class.DirectionType.INBOUND
    
    def __init__(self, dir_type=1, name="Generic Direction", tag=-1):
        self.type = dir_type
        self.name = name
        self.tag = tag
        self.stops = []
        
    def __str__(self):
        dir_type = 'Outbound'
        if self.type == Direction.DirectionType.INBOUND:
            dir_type = 'Inbound'
        return self.name + '(' + dir_type + ')' 
        
class Route(object):

    def __init__(self):
        self.name = ''
        self.tag = -1
        self.stops = []
        self.directions = []
        self.bounding_box = []
        
    def __str__(self):
        return self.name
        
    def find_stop(tag):
        return filter(lambda x: x.tag == tag, self.stops)[0]

# Functions
def send_request(url):
    result = None
    try:
    	result = urllib2.urlopen(url).read()
    except urllib2.HTTPError, e:
    	print "HTTP error: %d" % e.code
    except urllib2.URLError, e:
    	print "Network error: %s" % e.reason.args[1]
    	
    return result
    
def print_xml(xml_string):
    xml = parseString(xml_string)
    formatted_result = re.sub('[\t]\n{0,2}',' ',str(xml.toprettyxml()))
    print formatted_result
    
def connect_to_muni_test():
    print "Test to see if the Muni data is up."
    test_url = SF_MUNI_URL + 'routeList&a=sf-muni'
    
    print "Test url: " + test_url
    result = send_request(test_url)
    
    print "The result in xml form:"
    print_xml(result)
    
    print "The result from the xml library:"
    tree = xmlparser.fromstring(result)
    children = list(tree)
    for node in children:
        print node.tag, node.attrib
       
def simple_route_query_test():
    print "Test to get specific information about a route."
    routes_url = SF_MUNI_URL + 'routeList&a=sf-muni'
    route_detail_url = SF_MUNI_URL + 'routeConfig&a=sf-muni&r='
    
    print "Routes url: " + routes_url
    routes_result = send_request(routes_url)
    root = xmlparser.fromstring(routes_result)
    routes = list(root)
    
    # DO THIS FOR TESTING
    for route in routes[:1]:
        route_url = route_detail_url + route.attrib['tag']
    
        print "Route detail url: " + route_url
        route_detail_result = send_request(route_url)
        time.sleep(1)
        route = RouteParser.parse_route_from_xml(route_detail_result)
    	
if __name__ == "__main__":
    # Tests        
    #connect_to_muni_test()
    #time.sleep(1)
    #print ''
    simple_route_query_test()

	
