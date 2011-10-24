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
# Commands
# 1) "routeList"
# 2) "routeConfig"
# 3) "predictions"
# 4) "predictionsForMultiStops"
# 5) "vehicleLocations"
# 
# Command Examples
# 1) Get all routes
#    http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni
# 2) Get specific route information (in example 'F' is the route tag)
#    http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni&r=F
# 3) Get vehicle locations (in example 'N' is the route tag and '1144953500233' is the ms time of the last sample)
#    http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&r=N&t=1144953500233

# Libraries
import xml.etree.ElementTree as xmlparser
import urllib2
import time

# Constants

# Functions
def sendRequest(url):
    result = None
    try:
    	result = urllib2.urlopen(url).read()
    except urllib2.HTTPError, e:
    	print "HTTP error: %d" % e.code
    except urllib2.URLError, e:
    	print "Network error: %s" % e.reason.args[1]
    	
    return result
    
def connectionToMuniTest():
    test_url = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni"
    result = sendRequest(test_url)
    xml_root_element = xmlparser.fromstring(result)
    children = xml_root_element.getchildren()

    for node in children:
        print node.attrib
        
def simpleRouteQueryTest():
    base_url = "http://webservices.nextbus.com/service/publicXMLFeed"
    get_routes_url = base_url + "?command=routeList&a=sf-muni"
    get_route_detail_url = base_url + "?command=routeConfig&a=sf-muni&r="
    
    routes_result = sendRequest(get_routes_url)
    time.sleep(1)

# Tests        
connectionToMuniTest()
time.sleep(1)
simpleRouteQueryTest()

