# -----------------------------------------------------------------------------
#
#   XmlPointParser.py
#   By: Fred Stakem
#   Date: 12.9.11
#
#   Purpose: This is the xml point parser class for parsing Muni points.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
import XmlParser as XmlParser
import Location as Location

class XmlPointParser(XmlParser):
    
    POINT_TAG = "point"
    
    def __init__(self):
        pass
    def __init__(self):
        pass
        
    @staticmethod
    def get_object_from_xml(xml):
        points_xml = xml.findall(XmlPointParser.POINT_TAG)
        points = []
        for point_xml in points_xml:
            location = XmlPointParser.get_object_from_dict(point_xml)
            points.append(location)
            
        return points
        
    @staticmethod    
    def get_object_from_dict(values):
        location = Location()
        latitude = XmlParser.get_latitude(values)
        longitude = XmlParser.get_longitude(values)
        location = Location(latitude, longitude) 
        
        return location