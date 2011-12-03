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
import xml.etree.ElementTree as xmlparser
import urllib2
import time
import re
from xml.dom.minidom import parseString
from muniroutes.polls import Stops
from muniroutes.polls import BusLoc

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
    url = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictionsForMultiStops&a=sf-muni&stops=N|null|6997&stops=N|null|3909'
    
    result = sendRequest(url)
    printXML(result)
    
    return(0)
       
def simpleRouteQueryTest():
    base_url = "http://webservices.nextbus.com/service/publicXMLFeed"
    get_routes_url = base_url + "?command=routeList&a=sf-muni"
    get_route_detail_url = base_url + "?command=routeConfig&a=sf-muni&r="
    
    routes_result = sendRequest(get_routes_url)
    time.sleep(1)


def printXML(xml_string):
    xml = parseString(xml_string)
    formatted_result = re.sub('[\t]\n{0,2}',' ',str(xml.toprettyxml()))
    print formatted_result
    
    return(0)
    
    # Original
    xml_root_element = xmlparser.fromstring(xmlString)
    children = xml_root_element.getchildren()
    for node in children:
        node.attrib

# Return query data - whether from file or web
# FIX: http return requests do not work
def getQuery(name, type):
    if (name == 'bus_loc'):
        if (type == 'file'):
            return('bus_loc-publicXMLFeed.xml')
        elif (type == 'http'):
            result = sendRequest('http://webservices.nextbus.com/service/publicXMLFeed?command=vehicleLocations&a=sf-muni&t=0')
            return(result)
    elif (name == 'stops'):
        if (type == 'file'):
            return('all_stop-publicXMLFeed.xml')
        elif(type == 'http'):
            result = sendRequest('http://webservices.nextbus.com/service/publicXMLFeed?command=routeConfig&a=sf-muni')
            return(results)


# Create local DB selected  
def populateDB(type='none'):
    if (type == 'bus_loc'):
        source = getQuery('bus_loc','file')
        tree = xmlparser.parse(source)

        # For testing, clear out all old data prior to writing
        BusLoc.objects.all().delete()
        
        for parent in tree.iter('body'):
            for child in parent:
                if (child.tag == 'vehicle'):
                    print "DEBUG: [%s] [%s] [%s] [%s] [%s] [%s] [%s]\n"%(child.get('id'), child.get('routeTag'), child.get('dirTag'), child.get('lat'), child.get('lon'), child.get('secsSinceReport'), child.get('predictable') )            
                    curr_bus_loc = BusLoc(vehId=child.get('id'),routeTag=child.get('routeTag'),dirTag=child.get('dirTag'),lat=child.get('lat'),lon=child.get('lon'),secsSinceReport=child.get('secsSinceReport'),predictable=child.get('predictable'))
                    curr_bus_loc.save()
        return()
        
    elif (type == 'stops'):
        source = getQuery('stops','file')
        tree = xmlparser.parse(source)

        # For testing, clear out all old data prior to writing
        Stops.objects.all().delete()
        
        for parent in tree.iter('route'):
            print "DEBUG: %s %s\n"%(parent.tag, parent.get('tag'))
            for child in parent:
                if (child.tag == 'stop'):
                    print "DEBUG: [%s][%s] - [%s] [%s] [%s] [%s] [%s] [%s]\n"%(parent.tag,child.tag, child.get('tag'), child.get('title'), child.get('lat'), child.get('lon'), child.get('stopId'), parent.get('tag') )            
                    curr_stop = Stops(tag=child.get('tag'),title=child.get('title'),lat=child.get('lat'),lon=child.get('lon'),stopId=child.get('stopId'),route=parent.get('tag'))
                    curr_stop.save()
        return()
        
    else:
        print "Invalid type [%s]"%(type)
        return(1)    


# Given stop_tag, return object with query info from DB
def stopQuery():
    pass

# Given stop_tag, return next buses (each route being serviced)
def stopNextBuses():
    # use predictions command
    pass
    
# Given geo location, return object with closest stop_tag and distance per coord
def closestStop():
    pass
    
# Given geo location, return closest buses
def closestBus():
    # May want to periodically populate DB with all bus location info, then directly query DB for faster results
    pass


    
def main():
    # Tests        
    connectionToMuniTest()
    #time.sleep(1)
    #simpleRouteQueryTest()
    print "DONE main\n"
	
	
if __name__ == "__main__":
    main()

	
