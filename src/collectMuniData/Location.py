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

    def __str__(self):
        return '(' + str(self.latitude) + ', ' + str(self.longitude) + ')'
