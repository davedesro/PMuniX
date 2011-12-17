# -----------------------------------------------------------------------------
#
#   DirectionXmlParser.py
#   By: Fred Stakem
#   Created: 12.9.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the xml direction parser class for parsing Muni 
#            directions.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
from XmlParser import XmlParser
from Direction import Direction

class DirectionXmlParser(XmlParser):
    
    DIRECTION_TAG = "direction"
    STOP_TAG = "stop"
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
                
    @staticmethod
    def get_object_from_xml(xml, stops):
        directions_xml = xml.findall(DirectionXmlParser.DIRECTION_TAG)
        directions = []
        for direction_xml in directions_xml:
            direction = DirectionXmlParser.get_object_from_dict(direction_xml.attrib)
            stops_xml = direction_xml.findall(DirectionXmlParser.STOP_TAG)
            for stop_xml in stops_xml:
                tag = XmlParser.get_tag(stop_xml.attrib)
                stop = filter(lambda x: x.tag == int(tag), stops)[0]
                direction.stops.append(stop)
            directions.append(direction)
            
        return directions
    
    @staticmethod    
    def get_object_from_dict(values):
        direction = Direction()
        direction.type = XmlParser.get_direction_type(values)
        direction.name = XmlParser.get_title(values)
        direction.tag = XmlParser.get_tag(values)
        
        return direction