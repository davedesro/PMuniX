# -----------------------------------------------------------------------------
#
#   XmlParser.py
#   By: Fred Stakem
#   Date: 12.6.11
#
#   Purpose: This is the base class for a collection of classes that parse 
#            the Muni server feed.
#
# -----------------------------------------------------------------------------

# Import libs
import Util

# Import classes

class XmlParser(object):
    
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
    
    DirectionType = Util.enum(INBOUND=1, OUTBOUND=2)
    
    def __init__(self):
        pass
    
    def __str__(self):
        pass
        
    @staticmethod
    def get_objects_from_xml(xml):
        pass
     
    @staticmethod   
    def get_object_from_dict(values):
        pass
        
    @staticmethod
    def get_title(values):
        return values.get(XmlParser.TITLE_LABEL)

    @staticmethod
    def get_tag(values):
        return values.get(XmlParser.TAG_LABEL)
        
    @staticmethod
    def get_stop_id(values):
        return int( values.get(XmlParser.STOP_ID_LABEL) )
        
    @staticmethod
    def get_vehicle_id(values):
        return int( values.get(XmlParser.VEHICLE_ID_LABEL) )
        
    @staticmethod
    def get_route_tag(values):
        return values.get(XmlParser.ROUTE_TAG_LABEL)

    @staticmethod
    def get_latitude(values):
        return float( values.get(XmlParser.LATITUDE_LABEL) )

    @staticmethod
    def get_longitude(values):
        return float( values.get(XmlParser.LONGITUDE_LABEL) )
        
    @staticmethod
    def get_direction_type(values):
        if values.get(XmlParser.NAME_LABEL) == XmlParser.NAMES[0]:
            return XmlParser.DirectionType.INBOUND
        else:
            return XmlParser.DirectionType.OUTBOUND
              
    @staticmethod
    def get_heading(values):
        return int( values.get(XmlParser.HEADING_LABEL) )

    @staticmethod
    def get_speed(values):
        return float( values.get(XmlParser.SPEED_LABEL) )
            
