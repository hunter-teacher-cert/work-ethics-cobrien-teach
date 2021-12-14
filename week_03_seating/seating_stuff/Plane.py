"""
Encodes info about plane.
rows: total number of rows in the plane (plane always has 6 columns)
window: # available windows
aisle: # available aisles
middle: # available middle
"""
class plane:
    def __init__(self, r):
        self.rows = r;
        self.window = r*2
        self.aisle = r*2
        self.middle = r*2

    def buy_window(self):
        self.windows--

    def buy_aisle(self):
        self.aisle--

    def buy_middle(self):
        self.middle--
