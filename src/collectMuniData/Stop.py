# -----------------------------------------------------------------------------
#
#   Stop.py
#   By: Fred Stakem
#   Created: 12.6.11
#   Modified: 12.13.11
#
#   Purpose: This is the stop class for storing Muni stops.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
from Location import Location

class Stop(object):
    
    def __init__(self, stop_id=-1, name="Generic Stop", tag=-1, location=Location()):
        self.id = stop_id
        self.name = name
        self.tag = tag
        self.location = location
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
    
    def __str__(self):
        return self.name + '(' + str(self.id) + ') Location: ' + str(self.location)
