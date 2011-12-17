# -----------------------------------------------------------------------------
#
#   Path.py
#   By: Fred Stakem
#   Created: 12.13.11
#   Last Modified: 12.13.11
#
#   Purpose: This is the path class for all of the locations along a path.
#
# -----------------------------------------------------------------------------

# Import libs

# Import classes

class Path(object):
    
    def __init__(self):
        self.locations = []
        
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)

        
    def __str__(self):
        return "Number of locations: " + str(len(self.locations))