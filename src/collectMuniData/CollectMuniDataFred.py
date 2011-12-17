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

# Debug
TEST = 3

# Constants
SF_MUNI_URL = 'http://webservices.nextbus.com/service/publicXMLFeed?command='

# Helper functions
def enum(**enums):
    return type('Enum', (), enums)
    
def print_xml(xml_string):
    xml = parseString(xml_string)
    formatted_result = re.sub('[\t]\n{0,2}',' ',str(xml.toprettyxml()))
    print formatted_result

# Models   
class Parser(object):
    
    TITLE_LABEL = 'title'
    TAG_LABEL = 'tag'
    STOP_ID_LABEL = 'stopId'
    VEHICLE_ID_LABEL = 'id'
    ROUTE_TAG_LABEL = 'routeTag'
    LATITUDE_LABEL = 'lat'
    LONGITUDE_LABEL = 'lon'
    NAME_LABEL = 'name'
    LATITUDE_MIN_LABEL = 'latMin'
    LATITUDE_MAX_LABEL = 'latMax'
    LONGITUDE_MIN_LABEL = 'lonMin'
    LONGITUDE_MAX_LABEL = 'lonMax'
    HEADING_LABEL = 'heading'
    SPEED_LABEL = 'speedKmHr'
    
    NAMES = ['Inbound', 'Outbound']
    
    DirectionType = enum(INBOUND=1, OUTBOUND=2)
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass
        
    @staticmethod
    def get_object_from_xml(xml):
        pass
     
    @staticmethod   
    def get_object_from_dict(values):
        pass
        
    @staticmethod
    def get_title(values):
        return values.get(Parser.TITLE_LABEL)

    @staticmethod
    def get_tag(values):
        return values.get(Parser.TAG_LABEL)
        
    @staticmethod
    def get_stop_id(values):
        return int( values.get(Parser.STOP_ID_LABEL) )
        
    @staticmethod
    def get_vehicle_id(values):
        return int( values.get(Parser.VEHICLE_ID_LABEL) )
        
    @staticmethod
    def get_route_tag(values):
        return values.get(Parser.ROUTE_TAG_LABEL)

    @staticmethod
    def get_latitude(values):
        return float( values.get(Parser.LATITUDE_LABEL) )

    @staticmethod
    def get_longitude(values):
        return float( values.get(Parser.LONGITUDE_LABEL) )
        
    @staticmethod
    def get_direction_type(values):
        if values.get(Parser.NAME_LABEL) == Parser.NAMES[0]:
            return Parser.DirectionType.INBOUND
        else:
            return Parser.DirectionType.OUTBOUND
            
    @staticmethod
    def get_latitude_min(values):
        return float( values.get(RouteParser.LATITUDE_MIN_LABEL) )

    @staticmethod
    def get_latitude_max(values):
        return float( values.get(RouteParser.LATITUDE_MAX_LABEL) )

    @staticmethod
    def get_longitude_min(values):
        return float( values.get(RouteParser.LONGITUDE_MIN_LABEL) )

    @staticmethod
    def get_longitude_max(values):
        return float( values.get(RouteParser.LONGITUDE_MAX_LABEL) )

    @staticmethod
    def get_heading(values):
        return int( values.get(RouteParser.HEADING_LABEL) )
        
    @staticmethod
    def get_speed(values):
        return float( values.get(RouteParser.SPEED_LABEL) )

                    
class StopParser(Parser):
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    @staticmethod
    def get_object_from_xml(xml):
        stops_xml = xml.findall("stop")
        stops = []
        for stop_xml in stops_xml:
            stop = StopParser.get_object_from_dict(stop_xml.attrib)
            stops.append(stop)
            
        return stops
    
    @staticmethod    
    def get_object_from_dict(values):
        stop = Stop()
        stop.id = Parser.get_stop_id(values)
        stop.name = Parser.get_title(values)
        stop.tag = Parser.get_tag(values)
        latitude = Parser.get_latitude(values)
        longitude = Parser.get_longitude(values)
        location = Location(latitude, longitude)
        stop.location = location
        
        return stop
              
class PointParser(Parser):
    
    def __init__(self):
        pass
    def __init__(self):
        pass
        
    @staticmethod
    def get_object_from_xml(xml):
        points_xml = xml.findall("point")
        points = []
        for point_xml in points_xml:
            location = PointParser.get_object_from_dict(point_xml)
            points.append(location)
            
        return points
        
    @staticmethod    
    def get_object_from_dict(values):
        location = Location()
        latitude = Parser.get_latitude(values)
        longitude = Parser.get_longitude(values)
        location = Location(latitude, longitude) 
        
        return location
        
class PathParser(Parser):
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    @staticmethod
    def get_object_from_xlm(xml):
        paths_xml = xml.findall("path")
        paths = []
        for path_xml in paths_xml:
            points = PointParser.get_object_from_xml(path_xml)
            paths.append(points)
                
        return paths
        
    @staticmethod
    def get_object_from_dict(values):
        pass
                        
class DirectionParser(Parser):
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
                
    @staticmethod
    def get_object_from_xml(xml, route):
        directions_xml = xml.findall("direction")
        directions = []
        for direction_xml in directions_xml:
            direction = DirectionParser.get_object_from_dict(direction_xml.attrib)
            stops_xml = direction_xml.findall("stop")
            for stop_xml in stops_xml:
                tag = Parser.get_tag(stop_xml.attrib)
                stop = route.find_stop(tag)
                direction.stops.append(stop)
            directions.append(direction)
            
        return directions
    
    @staticmethod    
    def get_object_from_dict(values):
        direction = Direction()
        direction.type = Parser.get_direction_type(values)
        direction.name = Parser.get_title(values)
        direction.tag = Parser.get_tag(values)
        
        return direction
       
class RouteParser(Parser):
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
                
    @staticmethod
    def get_object_from_xml(xml):
        root_xml = xmlparser.fromstring(xml)
        route_xml = root_xml[0]
        route = RouteParser.get_object_from_dict(route_xml.attrib)
        route.stops = StopParser.get_object_from_xml(route_xml)
        route.directions = DirectionParser.get_object_from_xml(route_xml, route)
        route.paths = PathParser.get_object_from_xlm(route_xml)
        
        return route
              
    @staticmethod    
    def get_object_from_dict(values):
        route = Route()
        route.name = Parser.get_title(values)
        route.tag = Parser.get_tag(values)
        latitude_min = Parser.get_latitude_min(values)
        latitude_max = Parser.get_latitude_max(values)
        longitude_min = Parser.get_longitude_min(values)
        longtitude_max = Parser.get_longitude_max(values)
        route.bounding_box = [ [latitude_min, latitude_max], [longitude_min, longtitude_max] ]
        
        return route

class VehicleStateParser(Parser):
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    @staticmethod
    def get_object_from_xml(xml, vehicles, current_time):
        root_xml = xmlparser.fromstring(xml)
        vehicles_state_xml = root_xml.findall("vehicle")
        for vehicle_state_xml in vehicles_state_xml:
            vehicle_state = VehicleStateParser.get_object_from_dict(vehicle_state_xml.attrib)
            vehicle_state.time = current_time
            vehicle_id = Parser.get_vehicle_id(vehicle_state_xml.attrib)
            
            current_vehicles = filter(lambda x: x.id == vehicle_id, vehicles)
            if len(current_vehicles) != 0:
                current_vehicles[0].states.append(vehicle_state)
            else:
                route_tag = Parser.get_route_tag(vehicle_state_xml.attrib)
                vehicle = Vehicle(vehicle_id=vehicle_id, route=route_tag)
                vehicle.states.append(vehicle_state)
                vehicles.append(vehicle)
        
        return vehicles
        
    @staticmethod
    def get_object_from_dict(values):
        vehicle_state = VehicleState()
        latitude = Parser.get_latitude(values)
        longitude = Parser.get_longitude(values)
        location = Location(latitude=latitude, longitude=longitude)
        vehicle_state.location = location
        vehicle_state.heading = Parser.get_heading(values)
        vehicle_state.speed = Parser.get_speed(values)
           
        return vehicle_state
        
class Location(object):

    def __init__(self, latitude=0.0, longitude=0.0):
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '(' + str(self.latitude) + ', ' + str(self.longitude) + ')'
        
class VehicleState(Location):
    
    def __init__(self, time=-1, heading=0, location=Location(), speed_km_hr=0.0):
        self.time = time
        self.heading = heading
        self.location = location
        self.speed_km_hr = speed_km_hr
        
    def __str__(self):
        return str(self.time) + " Heading: " + str(self.heading) + " Location: " + str(self.location)
 
class Stop(object):
    
    def __init__(self, stop_id=-1, name="Generic Stop", tag=-1, location=Location()):
        self.id = stop_id
        self.name = name
        self.tag = tag
        self.location = location
        
    def __str__(self):
        return self.name + '(' + str(self.id) + ') Location: ' + str(self.location)
        
class Direction(object):
    
    def __init__(self, dir_type=1, name="Generic Direction", tag=-1):
        self.type = dir_type
        self.name = name
        self.tag = tag
        self.stops = []
        
    def __str__(self):
        dir_type = 'Outbound'
        if self.type == Parser.DirectionType.INBOUND:
            dir_type = 'Inbound'
        return self.name + '(' + dir_type + ')' 
        
class Path(object):
    
    def __init__(self):
        self.locations = []
        
    def __str__(self):
        return "Number of locations: " + str(len(self.locations))
        
class Route(object):

    def __init__(self):
        self.name = ''
        self.tag = -1
        self.stops = []
        self.directions = []
        self.bounding_box = []
        self.paths = []
        self.vehicles = []
        
    def __str__(self):
        return self.name
        
    def route_to_string(self):
        output = self.name + "\n"
        output += "Directions: " + "\n"
        for direction in self.directions:
            output += "\t" + str(direction) + "\n"
        output += "Number of paths: " + str(len(self.paths)) + "\n"
        output += "Number of vehicles: " + str(len(self.vehicles)) + "\n"
        output += "Stops:"
        for stop in self.stops:
            output += "\t" + str(stop) + "\n"
            
        return output
            
    def vehicles_to_string(self):
        output = "Vehicles:" + "\n"
        for vehicle in self.vehicles:
            output += "\t" + str(vehicle) + "\n"
        return output
        
    def stops_to_string(self):
        pass    
    
    def paths_to_string(self):
        pass
        
    def find_stop(self, tag):
        return filter(lambda x: x.tag == tag, self.stops)[0]
        
class Vehicle(object):
    
    def __init__(self, vehicle_id=1, route="Generic Route"):
        self.id = vehicle_id
        self.route = route
        self.states  = []
        
    def __str__(self):
        return str(self.id) + ' Route: ' + str(self.route) + ' Current State: ' + str(self.states[-1])
        
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
    
    # Select only first value for testing
    for route in routes[:1]:
        route_url = route_detail_url + route.attrib['tag']
    
        print "Route detail url: " + route_url
        route_detail_result = send_request(route_url)
        time.sleep(1)
        route = RouteParser.get_object_from_xml(route_detail_result)
        print route.route_to_string()
        
def get_vehicle_locations():
    print "Test to get the current location of the buses."
    routes_url = SF_MUNI_URL + 'routeList&a=sf-muni'
    route_detail_url = SF_MUNI_URL + 'routeConfig&a=sf-muni&r='
    vehicle_url_base = SF_MUNI_URL + 'vehicleLocations&a=sf-muni&r='
    last_time = 0
    
    print "Routes url: " + routes_url
    routes_result = send_request(routes_url)
    root = xmlparser.fromstring(routes_result)
    routes = list(root)
    
    # Select only first value for testing
    for route in routes[:1]:
        route_url = route_detail_url + route.attrib['tag']
        vehicle_url = vehicle_url_base + route.attrib['tag'] + '&t=' + str(last_time)
        
        print "Route detail url: " + route_url
        route_detail_result = send_request(route_url)
        time.sleep(1)
        route = RouteParser.get_object_from_xml(route_detail_result)
        print route.route_to_string()
        
        print "Bus detail url: " + vehicle_url
        vehicle_detail_result = send_request(vehicle_url)
        time.sleep(1)
        current_time = 1000
        route.vehicles = VehicleStateParser.get_object_from_xml(vehicle_detail_result, route.vehicles, current_time)
        print route.vehicles_to_string()
       
       	
if __name__ == "__main__":
    # Tests        
    if TEST == 1:
        connect_to_muni_test()
    elif TEST == 2:
        simple_route_query_test()
    elif TEST == 3:
        get_vehicle_locations()

	
