# -----------------------------------------------------------------------------
#
#   RouteXmlParser.py
#   By: Fred Stakem
#   Created: 12.9.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the xml route parser class for parsing Muni 
#            routes.
#
# -----------------------------------------------------------------------------

# Import libs
import xml.etree.ElementTree as xmlLib

# Import classes
from XmlParser import XmlParser
from StopXmlParser import StopXmlParser
from DirectionXmlParser import DirectionXmlParser
from PathXmlParser import PathXmlParser
from Route import Route

class RouteXmlParser(XmlParser):
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    @staticmethod
    def get_latitude_min(values):
        return float( values.get(RouteXmlParser.LATITUDE_MIN_LABEL) )

    @staticmethod
    def get_latitude_max(values):
        return float( values.get(RouteXmlParser.LATITUDE_MAX_LABEL) )

    @staticmethod
    def get_longitude_min(values):
        return float( values.get(RouteXmlParser.LONGITUDE_MIN_LABEL) )

    @staticmethod
    def get_longitude_max(values):
        return float( values.get(RouteXmlParser.LONGITUDE_MAX_LABEL) )
  
    @staticmethod
    def get_route_tag_from_list(xml, index=0):
        root = xmlLib.fromstring(xml)
        routes = list(root)
        
        if index >= 0 and index < len(routes):
            return routes[index].attrib['tag']
        else:
            return ""
                
    @staticmethod
    def get_object_from_xml(xml):
        root_xml = xmlLib.fromstring(xml)
        route_xml = root_xml[0]
        route = RouteXmlParser.get_object_from_dict(route_xml.attrib)
        route.stops = StopXmlParser.get_object_from_xml(route_xml)
        route.directions = DirectionXmlParser.get_object_from_xml(route_xml, route.stops)
        route.paths = PathXmlParser.get_object_from_xml(route_xml)
        
        return route
              
    @staticmethod    
    def get_object_from_dict(values):
        route = Route()
        route.name = XmlParser.get_title(values)
        route.tag = XmlParser.get_tag(values)
        latitude_min = RouteXmlParser.get_latitude_min(values)
        latitude_max = RouteXmlParser.get_latitude_max(values)
        longitude_min = RouteXmlParser.get_longitude_min(values)
        longtitude_max = RouteXmlParser.get_longitude_max(values)
        route.bounding_box = [ [latitude_min, latitude_max], [longitude_min, longtitude_max] ]
        
        return route