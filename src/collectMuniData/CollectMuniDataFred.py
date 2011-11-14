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
    first_route = routes[0]
    route_detail_url = route_detail_url + first_route.attrib['tag']
    time.sleep(1)
    
    print "Route detail url: " + route_detail_url
    route_detail_result = send_request(route_detail_url)
    
    print "The result in xml form:"
    print_xml(route_detail_result)
    
    print "The result from the xml library:"
    root = xmlparser.fromstring(route_detail_result)
    route = list(root)
    print route[0].tag, route[0].attrib
    stops = root.findall("route/stop")
    for stop in stops:
        print "  ", stop.tag, stop.attrib
        
    directions = root.findall("route/direction")
    for direction in directions:
        print "  ", direction.tag, direction.attrib
        stops = direction.findall("stop")
        for stop in stops:
            print "  ", "  ", stop.tag, stop.attrib
        
    paths = root.findall("route/path")
    for path in paths:
        print "  ", path.tag, path.attrib
        points = path.findall("point")
        for point in points:
            print "  ", "  ", point.tag, point.attrib
    	
if __name__ == "__main__":
    # Tests        
    connect_to_muni_test()
    time.sleep(1)
    print ''
    simple_route_query_test()

	
