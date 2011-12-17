# -----------------------------------------------------------------------------
#
#   RouteXmlParserTest.py
#   By: Fred Stakem
#   Created: 12.15.11
#   Last Modified: 12.15.11
#
#   Purpose: This is the xml route parser test class for parsing Muni 
#            routes.
#
# -----------------------------------------------------------------------------

# Import libs
import unittest

# Import classes
from XmlParser import XmlParser
from StopXmlParser import StopXmlParser
from DirectionXmlParser import DirectionXmlParser
from PathXmlParser import PathXmlParser
from RouteXmlParser import RouteXmlParser
from Route import Route

class RouteXmlParserTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_route_tag_from_list(self):
        routes = [ "F", "J", "KT"]
        xml = """<?xml version="1.0" encoding="utf-8" ?>
                 <body copyright="All data copyright San Francisco Muni 2011.">
                 <route tag="%s" title="F-Market &amp; Wharves"/>
                 <route tag="%s" title="J-Church"/>
                 <route tag="%s" title="KT-Ingleside/Third Street"/>
                 </body>""" % (routes[0], routes[1], routes[2])
                  
        result = RouteXmlParser.get_route_tag_from_list(xml, 0)
        self.assertEqual(result, routes[0])
        result = RouteXmlParser.get_route_tag_from_list(xml, 1)
        self.assertEqual(result, routes[1])
        result = RouteXmlParser.get_route_tag_from_list(xml, 2)
        self.assertEqual(result, routes[2])
        result = RouteXmlParser.get_route_tag_from_list(xml, 3)
        self.assertEqual(result, "")
                  
        
    def test_get_object_from_xml(self):
        tag = "F"
        name = "F-Market &amp; Wharves"
        name_transformed = "F-Market & Wharves"
        latitude_min = "30.5"
        latitude_max = "40.5"
        longitude_min = "50.5"
        longtitude_max = "60.5"
        xml = """<?xml version="1.0" encoding="utf-8" ?> 
                 <body copyright="All data copyright San Francisco Muni 2011.">
                 <route tag="%s" title="%s" color="555555" oppositeColor="ffffff" latMin="%s" latMax="%s" lonMin="%s" lonMax="%s">
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
                 </body>""" % (tag, name, latitude_min, latitude_max, longitude_min, longtitude_max)
        
        route = RouteXmlParser.get_object_from_xml(xml)
        self.assertEqual(route.name, name_transformed)
        self.assertEqual(route.tag, tag)
        self.assertEqual(route.bounding_box[0][0], float(latitude_min))
        self.assertEqual(route.bounding_box[0][1], float(latitude_max))
        self.assertEqual(route.bounding_box[1][0], float(longitude_min))
        self.assertEqual(route.bounding_box[1][1], float(longtitude_max))
    
    
if __name__ == '__main__':
    unittest.main()