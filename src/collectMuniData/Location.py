# -----------------------------------------------------------------------------
#
#   Location.py
#   By: Fred Stakem
#   Created: 12.9.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the location class for storing world locations.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes

class Location(object):

    def __init__(self, latitude=0.0, longitude=0.0):
        self.latitude = latitude
        self.longitude = longitude
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return '(' + str(self.latitude) + ', ' + str(self.longitude) + ')'
