# -----------------------------------------------------------------------------
#
#   VehicleState.py
#   By: Fred Stakem
#   Created: 12.13.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the vehicle state class for a buses state.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
from Location import Location

class VehicleState(Location):
    
    def __init__(self, time=-1, heading=0, location=Location(), speed_km_hr=0.0):
        self.time = time
        self.heading = heading
        self.location = location
        self.speed_km_hr = speed_km_hr
        
    def __str__(self):
        return str(self.time) + " Heading: " + str(self.heading) + " Location: " + str(self.location)
