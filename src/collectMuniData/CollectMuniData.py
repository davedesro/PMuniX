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

# Libraries
import xml.etree.ElementTree as xmlparser
import urllib2  

# Constants

# Functions
def testConnectionToMuni():
    test_url = "http://webservices.nextbus.com/service/publicXMLFeed?command=routeList&a=sf-muni"
    try:
    	result = urllib2.urlopen(test_url).read()
    except urllib2.HTTPError, e:
    	print "HTTP error: %d" % e.code
    except urllib2.URLError, e:
    	print "Network error: %s" % e.reason.args[1]

    xml_root_element = xmlparser.fromstring(result)
    children = xml_root_element.getchildren()

    for node in children:
        print node.attrib

# Tests        
testConnectionToMuni()

