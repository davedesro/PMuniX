# -----------------------------------------------------------------------------
#
#   StopXmlParser.py
#   By: Fred Stakem
#   Created: 12.6.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the xml stop parser class for parsing Muni stops.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
import XmlParser as XmlParser
import StopXmlParser as StopXmlParser
import Stop as Stop
import Location as Location

class StopXmlParser(XmlParser):
    
    STOP_TAG = "stop"
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    @staticmethod
    def get_objects_from_xml(xml):
        stops_xml = xml.findall(XmlStopParser.STOP_TAG)
        stops = []
        for stop_xml in stops_xml:
            stop = StopXmlParser.get_object_from_dict(stop_xml.attrib)
            stops.append(stop)
            
        return stops
    
    @staticmethod    
    def get_object_from_dict(values):
        stop = Stop()
        stop.id = XmlParser.get_stop_id(values)
        stop.name = XmlParser.get_title(values)
        stop.tag = XmlParser.get_tag(values)
        latitude = XmlParser.get_latitude(values)
        longitude = XmlParser.get_longitude(values)
        location = Location(latitude, longitude)
        stop.location = location
        
        return stop