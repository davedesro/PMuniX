# -----------------------------------------------------------------------------
#
#   Route.py
#   By: Fred Stakem
#   Created: 12.13.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the route class which is the main class for a bus
#            route.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes

class Route(object):

    def __init__(self):
        self.name = ''
        self.tag = -1
        self.stops = []
        self.directions = []
        self.bounding_box = []
        self.paths = []
        self.vehicles = []
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
        
    def __str__(self):
        return self.name
        
    def route_to_string(self):
        output = self.name + "\n"
        output += "Directions: " + "\n"
        for direction in self.directions:
            output += "\t" + str(direction) + "\n"
        output += "Number of paths: " + str(len(self.paths)) + "\n"
        output += "Number of vehicles: " + str(len(self.vehicles)) + "\n"
        output += "Stops:"
        for stop in self.stops:
            output += "\t" + str(stop) + "\n"
            
        return output
            
    def vehicles_to_string(self):
        output = "Vehicles:" + "\n"
        for vehicle in self.vehicles:
            output += "\t" + str(vehicle) + "\n"
        return output
        
    def stops_to_string(self):
        pass    
    
    def paths_to_string(self):
        pass
        