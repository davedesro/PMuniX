# -----------------------------------------------------------------------------
#
#   PointXmlParserTest.py
#   By: Fred Stakem
#   Created: 12.16.11
#   Last Modified: 12.16.11
#
#   Purpose: This is the xml point parser test class for parsing Muni 
#            locations.
#
# -----------------------------------------------------------------------------

# Import libs
import unittest
import xml.etree.ElementTree as xmlLib

# Import classes
from XmlParser import XmlParser
from PointXmlParser import PointXmlParser
from Location import Location

class PointXmlParserTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_get_object_from_xml(self):
        locations = [ Location(30.5, 40.5), Location(50.5, 60.5), Location(70.5, 80.5) ]
        xml = """<path>
                    <point lat="%s" lon="%s"/>
                    <point lat="%s" lon="%s"/>
                    <point lat="%s" lon="%s"/>
                 </path>""" % ( locations[0].latitude, locations[0].longitude, 
                                locations[1].latitude, locations[1].longitude,
                                locations[2].latitude, locations[2].longitude )
        
        root_xml = xmlLib.fromstring(xml)
        parsed_locations = PointXmlParser.get_object_from_xml(root_xml)
        self.assertEqual(len(parsed_locations), 3)
        self.assertEqual(parsed_locations[0], locations[0])
        self.assertEqual(parsed_locations[1], locations[1])
        self.assertEqual(parsed_locations[2], locations[2])
               
if __name__ == '__main__':
    unittest.main()