"""
Encodes information about each passenger:
name: name of the passenger
seat_type: window, aisle, middle
"""
class Passenger:
    def __init__(self, n, s):
        self.name = n;
        self.seat_type = s;
        self.actual_seat = null;

    def getName(self):
        return self.name;

    def getSeatType(self):
        return self.seat_type
    # fred = Passenger("Fred", "middle")
    # fred.getName() = "Fred"
