# -----------------------------------------------------------------------------
#
#   PathXmlParserTest.py
#   By: Fred Stakem
#   Created: 12.16.11
#   Last Modified: 12.16.11
#
#   Purpose: This is the xml path parser test class for parsing Muni 
#            paths.
#
# -----------------------------------------------------------------------------

# Import libs
import unittest
import xml.etree.ElementTree as xmlLib

# Import classes
from XmlParser import XmlParser
from PathXmlParser import PathXmlParser

class PathXmlParserTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_get_object_from_xml(self):
        xml = """<?xml version="1.0" encoding="utf-8" ?> 
                 <body copyright="All data copyright San Francisco Muni 2011.">
                 <route tag="F" title="F-Market &amp; Wharves" color="555555" oppositeColor="ffffff" latMin="30.5" latMax="30.5" lonMin="30.5" lonMax="30.5">
                 <stop tag="5184" title="Jones St &amp; Beach St" lat="37.8072499" lon="-122.41737" stopId="15184"/>
                 <stop tag="3092" title="Beach St &amp; Mason St" lat="37.80741" lon="-122.4141199" stopId="13092"/>
                 <direction tag="F__OBCTRO" title="Outbound to Castro Station via Downtown" name="Outbound" useForUI="true">
                     <stop tag="5184" />
                     <stop tag="3092" />
                 </direction>
                 <direction tag="F__IBCTRO" title="Inbound to Fisherman&apos;s Wharf via Downtown" name="Inbound" useForUI="true">
                    <stop tag="5184" />
                    <stop tag="3092" />
                 </direction>
                 <path>
                    <point lat="37.76726" lon="-122.42915"/>
                    <point lat="37.76888" lon="-122.4271"/>
                    <point lat="37.77057" lon="-122.42497"/>
                 </path>
                 <path>
                    <point lat="37.76726" lon="-122.42915"/>
                    <point lat="37.76888" lon="-122.4271"/>
                    <point lat="37.77057" lon="-122.42497"/>
                 </path>
                 </route>
                 </body>""" 
        
        root_xml = xmlLib.fromstring(xml)
        route_xml = root_xml[0]
        paths = PathXmlParser.get_object_from_xml(route_xml)
        self.assertEqual(len(paths), 2)
               
if __name__ == '__main__':
    unittest.main()