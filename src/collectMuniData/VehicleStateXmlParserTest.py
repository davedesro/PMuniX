# -----------------------------------------------------------------------------
#
#   VehicleStateXmlParserTest.py
#   By: Fred Stakem
#   Created: 12.16.11
#   Last Modified: 12.16.11
#
#   Purpose: This is the xml vehicle state parser test class for parsing Muni 
#            bus states.
#
# -----------------------------------------------------------------------------

# Import libs
import unittest
import xml.etree.ElementTree as xmlLib

# Import classes
from XmlParser import XmlParser
from VehicleStateXmlParser import VehicleStateXmlParser
from VehicleState import VehicleState
from Location import Location
from Vehicle import Vehicle

class VehicleStateXmlParserTest(unittest.TestCase):
    
    def setUp(self):
        unittest.TestCase.setUp(self)

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def test_get_object_from_xml(self):
        # (self, time=-1, heading=0, location=Location(), speed_km_hr=0.0):
        # (self, vehicle_id=1, route="Generic Route")
        time = 1000
        vehicle_states = [ VehicleState(time, 10, Location(10.5, 20.5), 30.5),  
                           VehicleState(time, 20, Location(40.5, 50.5), 60.5) ]
        vehicles = [ Vehicle(1, "route A"), Vehicle(2, "route A") ]
        xml = """<?xml version="1.0" encoding="utf-8" ?> 
                 <body copyright="All data copyright San Francisco Muni 2011.">
                    <vehicle id="%s" routeTag="%s" dirTag="F__OBNOE" lat="%s" lon="%s" secsSinceReport="8" predictable="true" heading="%s" speedKmHr="%s"/>
                    <vehicle id="%s" routeTag="%s" dirTag="F__IBCTRO" lat="%s" lon="%s" secsSinceReport="72" predictable="true" heading="%s" speedKmHr="%s"/>
                    <lastTime time="1324093795592"/>
                 </body>""" % ( str(vehicles[0].id), vehicles[0].route, str(vehicle_states[0].location.latitude), 
                                str(vehicle_states[0].location.longitude), str(vehicle_states[0].heading), 
                                str(vehicle_states[0].speed_km_hr),
                                str(vehicles[1].id), vehicles[1].route, str(vehicle_states[1].location.latitude), 
                                str(vehicle_states[1].location.longitude), str(vehicle_states[1].heading), 
                                str(vehicle_states[1].speed_km_hr) )
        
        root_xml = xmlLib.fromstring(xml)
        vehicles_xml = root_xml[0]
        parsed_vehicles = VehicleStateXmlParser.get_object_from_xml(vehicles_xml, vehicles, time)
        self.assertEqual(parsed_vehicles[0].states[0], vehicle_states[0])
        self.assertEqual(parsed_vehicles[1].states[0], vehicle_states[1])
        
        
if __name__ == '__main__':
    unittest.main()