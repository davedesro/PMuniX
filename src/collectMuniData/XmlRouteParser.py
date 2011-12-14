# -----------------------------------------------------------------------------
#
#   XmlRouteParser.py
#   By: Fred Stakem
#   Date: 12.9.11
#
#   Purpose: This is the xml route parser class for parsing Muni 
#   routes.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
import XmlParser as XmlParser

class XmlRouteParser(XmlParser):
    
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
        route.name = XmlParser.get_title(values)
        route.tag = XmlParser.get_tag(values)
        latitude_min = XmlParser.get_latitude_min(values)
        latitude_max = XmlParser.get_latitude_max(values)
        longitude_min = XmlParser.get_longitude_min(values)
        longtitude_max = XmlParser.get_longitude_max(values)
        route.bounding_box = [ [latitude_min, latitude_max], [longitude_min, longtitude_max] ]
        
        return route