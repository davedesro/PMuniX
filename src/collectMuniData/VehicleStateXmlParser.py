# -----------------------------------------------------------------------------
#
#   VehicleStateXmlParser.py
#   By: Fred Stakem
#   Created: 12.13.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the xml direction parser class for parsing the state 
#            of Muni buses. 
#
# -----------------------------------------------------------------------------

# Import libs
import xml.etree.ElementTree as xmlLib

# Import classes
from XmlParser import XmlParser
from Vehicle import Vehicle
from VehicleState import VehicleState
from Location import Location

class VehicleStateXmlParser(XmlParser):
    
    VEHICLE_TAG = "vehicle"
    
    def __init__(self):
        pass
        
    def __str__(self):
        pass
        
    @staticmethod
    def get_object_from_xml(xml, vehicles, current_time):
        root_xml = xmlLib.fromstring(xml)
        vehicles_state_xml = root_xml.findall(VehicleStateXmlParser.VEHICLE_TAG)
        for vehicle_state_xml in vehicles_state_xml:
            vehicle_state = VehicleStateXmlParser.get_object_from_dict(vehicle_state_xml.attrib)
            vehicle_state.time = current_time
            vehicle_id = XmlParser.get_vehicle_id(vehicle_state_xml.attrib)
            
            current_vehicles = filter(lambda x: x.id == vehicle_id, vehicles)
            if len(current_vehicles) != 0:
                current_vehicles[0].states.append(vehicle_state)
            else:
                route_tag = XmlParser.get_route_tag(vehicle_state_xml.attrib)
                vehicle = Vehicle(vehicle_id=vehicle_id, route=route_tag)
                vehicle.states.append(vehicle_state)
                vehicles.append(vehicle)
        
        return vehicles
        
    @staticmethod
    def get_object_from_dict(values):
        vehicle_state = VehicleState()
        latitude = XmlParser.get_latitude(values)
        longitude = XmlParser.get_longitude(values)
        location = Location(latitude=latitude, longitude=longitude)
        vehicle_state.location = location
        vehicle_state.heading = XmlParser.get_heading(values)
        vehicle_state.speed = XmlParser.get_speed(values)
           
        return vehicle_state