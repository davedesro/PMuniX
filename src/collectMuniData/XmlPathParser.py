# -----------------------------------------------------------------------------
#
#   XmlPathParser.py
#   By: Fred Stakem
#   Date: 12.9.11
#
#   Purpose: This is the xml path parser class for parsing Muni paths.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
import XmlParser as XmlParser
import Location as Location

class XmlPathParser(XmlParser):
    
    PATH_TAG = "path"
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    @staticmethod
    def get_object_from_xml(xml):
        paths_xml = xml.findall(XmlPathParser.PATH_TAG)
        paths = []
        for path_xml in paths_xml:
            points = XmlPointParser.get_object_from_xml(path_xml)
            paths.append(points)
                
        return paths
        
    @staticmethod
    def get_object_from_dict(values):
        pass