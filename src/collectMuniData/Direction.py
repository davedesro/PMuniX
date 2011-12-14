# -----------------------------------------------------------------------------
#
#   Direction.py
#   By: Fred Stakem
#   Created: 12.13.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the direction class for a route's direction.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes
from XmlParser import XmlParser

class Direction(object):
    
    def __init__(self, dir_type=1, name="Generic Direction", tag=-1):
        self.type = dir_type
        self.name = name
        self.tag = tag
        self.stops = []
        
    def __str__(self):
        dir_type = 'Outbound'
        if self.type == XmlParser.DirectionType.INBOUND:
            dir_type = 'Inbound'
        return self.name + '(' + dir_type + ')'