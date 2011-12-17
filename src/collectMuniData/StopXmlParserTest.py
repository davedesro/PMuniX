# -----------------------------------------------------------------------------
#
#   StopXmlParserTest.py
#   By: Fred Stakem
#   Created: 12.15.11
#   Last Modified: 12.15.11
#
#   Purpose: This is the xml route parser test class for parsing Muni 
#            stops.
#
# -----------------------------------------------------------------------------

# Import libs
import unittest
import xml.etree.ElementTree as xmlLib

# Import classes
from XmlParser import XmlParser
from StopXmlParser import StopXmlParser

class StopXmlParserTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_get_object_from_xml(self):
        stops = [ { 'tag': '5184', 'name': 'Jones St &amp; Beach St', 'name_transformed': 'Jones St & Beach St', 
                    'latitude': '30.5', 'longitude': '40.5', 'stop_id':'15184'}, 
                  { 'tag': '3092', 'name': 'Beach St &amp; Mason St', 'name_transformed': 'Beach St & Mason St', 
                    'latitude': '50.5', 'longitude': '60.5', 'stop_id':'3092'} ]
        xml = """<?xml version="1.0" encoding="utf-8" ?> 
                 <body copyright="All data copyright San Francisco Muni 2011.">
                 <route tag="F" title="F-Market &amp; Wharves" color="555555" oppositeColor="ffffff" latMin="30.5" latMax="30.5" lonMin="30.5" lonMax="30.5">
                 <stop tag="%s" title="%s" lat="%s" lon="%s" stopId="%s"/>
                 <stop tag="%s" title="%s" lat="%s" lon="%s" stopId="%s"/>
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
                 </body>""" % ( stops[0]['tag'], stops[0]['name'], stops[0]['latitude'], stops[0]['longitude'], stops[0]['stop_id'],
                                stops[1]['tag'], stops[1]['name'], stops[1]['latitude'], stops[1]['longitude'], stops[1]['stop_id'])
        
        root_xml = xmlLib.fromstring(xml)
        route_xml = root_xml[0]                        
        parsed_stops = StopXmlParser.get_object_from_xml(route_xml)
        for i, parsed_stop in enumerate(parsed_stops):
            self.assertEqual(parsed_stop.tag, stops[i]['tag'])
            self.assertEqual(parsed_stop.name, stops[i]['name_transformed'])
            self.assertEqual(parsed_stop.location.latitude, float(stops[i]['latitude']))
            self.assertEqual(parsed_stop.location.longitude, float(stops[i]['longitude']))
            self.assertEqual(parsed_stop.id, int(stops[i]['stop_id']))
        
        
if __name__ == '__main__':
    unittest.main()