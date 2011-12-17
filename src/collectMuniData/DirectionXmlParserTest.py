# -----------------------------------------------------------------------------
#
#   DirectionXmlParserTest.py
#   By: Fred Stakem
#   Created: 12.16.11
#   Last Modified: 12.16.11
#
#   Purpose: This is the xml direction parser test class for parsing Muni 
#            directions.
#
# -----------------------------------------------------------------------------

# Import libs
import unittest
import xml.etree.ElementTree as xmlLib

# Import classes
from XmlParser import XmlParser
from DirectionXmlParser import DirectionXmlParser
from Stop import Stop

class DirectionXmlParserTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_get_object_from_xml(self):
        tag = "F__OBCTRO"
        name = "Outbound to Castro Station via Downtown"
        dir_type = "Outbound"
        dir_type_enum = XmlParser.DirectionType.OUTBOUND
        stops = [ Stop(tag=5184), Stop(tag=3092) ]
        xml = """<?xml version="1.0" encoding="utf-8" ?> 
                 <body copyright="All data copyright San Francisco Muni 2011.">
                 <route tag="F" title="F-Market &amp; Wharves" color="555555" oppositeColor="ffffff" latMin="30.5" latMax="30.5" lonMin="30.5" lonMax="30.5">
                 <stop tag="5184" title="Jones St &amp; Beach St" lat="37.8072499" lon="-122.41737" stopId="15184"/>
                 <stop tag="3092" title="Beach St &amp; Mason St" lat="37.80741" lon="-122.4141199" stopId="13092"/>
                 <direction tag="%s" title="%s" name="%s" useForUI="true">
                    <stop tag="%s" />
                    <stop tag="%s" />
                 </direction>
                 <direction tag="F__IBCTRO" title="Inbound to Fisherman&apos;s Wharf via Downtown" name="Inbound" useForUI="true">
                    <stop tag="5184" />
                    <stop tag="3092" />
                 </direction>
                 <path>
                    <point lat="37.7678299" lon="-122.42863"/>
                    <point lat="37.76619" lon="-122.43071"/>
                    <point lat="37.76449" lon="-122.43281"/>
                 </path>
                 <path>
                    <point lat="37.76726" lon="-122.42915"/>
                    <point lat="37.76888" lon="-122.4271"/>
                    <point lat="37.77057" lon="-122.42497"/>
                 </path>
                 </route>
                 </body>""" % (tag, name, dir_type, str(stops[0].tag), str(stops[1].tag))
        
        root_xml = xmlLib.fromstring(xml)
        route_xml = root_xml[0]
        directions = DirectionXmlParser.get_object_from_xml(route_xml, stops)
        self.assertEqual(directions[0].tag, tag)
        self.assertEqual(directions[0].name, name)
        self.assertEqual(directions[0].type, dir_type_enum)
        self.assertEqual(directions[0].stops[0].tag, stops[0].tag)
        self.assertEqual(directions[0].stops[1].tag, stops[1].tag)
        
if __name__ == '__main__':
    unittest.main()