# -----------------------------------------------------------------------------
#
#   PathXmlParser.py
#   By: Fred Stakem
#   Created: 12.9.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the xml path parser class for parsing Muni paths.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
from XmlParser import XmlParser
from PointXmlParser import PointXmlParser
from Location import Location

class PathXmlParser(XmlParser):
    
    PATH_TAG = "path"
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    @staticmethod
    def get_object_from_xml(xml):
        paths_xml = xml.findall(PathXmlParser.PATH_TAG)
        paths = []
        for path_xml in paths_xml:
            points = PointXmlParser.get_object_from_xml(path_xml)
            paths.append(points)
                
        return paths
        
    @staticmethod
    def get_object_from_dict(values):
        pass