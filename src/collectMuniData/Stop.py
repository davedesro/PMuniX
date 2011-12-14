# -----------------------------------------------------------------------------
#
#   Stop.py
#   By: Fred Stakem
#   Date: 12.6.11
#
#   Purpose: This is the stop class for storing Muni stops.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
import Location as Location

class Stop(object):
    
    def __init__(self, stop_id=-1, name="Generic Stop", tag=-1, location=Location()):
        self.id = stop_id
        self.name = name
        self.tag = tag
        self.location = location
        
    def __str__(self):
        return self.name + '(' + str(self.id) + ') Location: ' + str(self.location)
