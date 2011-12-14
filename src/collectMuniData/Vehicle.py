# -----------------------------------------------------------------------------
#
#   Vehicle.py
#   By: Fred Stakem
#   Created: 12.13.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the vehicle class for all Muni buses.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes

class Vehicle(object):
    
    def __init__(self, vehicle_id=1, route="Generic Route"):
        self.id = vehicle_id
        self.route = route
        self.states  = []
        
    def __str__(self):
        return str(self.id) + ' Route: ' + str(self.route) + ' Current State: ' + str(self.states[-1])