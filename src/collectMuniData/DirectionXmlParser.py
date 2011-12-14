# -----------------------------------------------------------------------------
#
#   XmlDirectionParser.py
#   By: Fred Stakem
#   Date: 12.9.11
#
#   Purpose: This is the xml direction parser class for parsing Muni 
#   directions.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
import XmlParser as XmlParser

class XmlDirectionParser(XmlParser):
    
    DIRECTION_TAG = "direction"
    STOP_TAG = "stop"
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
                
    @staticmethod
    def get_object_from_xml(xml, route):
        directions_xml = xml.findall(XmlDirectionParser.DIRECTION_TAG)
        directions = []
        for direction_xml in directions_xml:
            direction = XmlDirectionParser.get_object_from_dict(direction_xml.attrib)
            stops_xml = direction_xml.findall(XmlDirectionParser.STOP_TAG)
            for stop_xml in stops_xml:
                tag = XmlParser.get_tag(stop_xml.attrib)
                stop = route.find_stop(tag)
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