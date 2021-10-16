"""
Plane seating algoithm.
Worked on w/ Emma Wingreen.
Algo Works on a first come first serve basis. If desired seat is check_available
you get it, otherwise you pick something else. No distinctions between classes.
No bulk purchasing.  
"""

#pointers will be Incremented as seats are purchased
pointer = {
"window":0,
"middle":0,
"aisle":0
}
# num of rows in plane
rows = 10;
def create_plane(rows):
    """
    A dict of of 3 row*2-length lists, representing window, aisle, middle seats.
    There are 2*rows for each seat type.
    """
    plane = {
        "window": ["window"]*rows*2,
        "middle": ["middle"]*rows*2,
        "aisle": ["aisle"]*rows*2
    }

    return plane

def print_plane(plane):
    """
    prints out seats in a plane with n rows and 6 columns distributed as
    window middle aisle   aisle middle window
    """
    s = ""
    for i in range(rows):
        w = plane["window"][i]
        m = plane["middle"][i]
        a = plane["aisle"][i]
        w2 = plane["window"][i+rows]
        m2 = plane["middle"][i+rows]
        a2 = plane["aisle"][i+rows]
        s  += w + " " + m + " " + a + "   " + a2 + " " + m2 + " " + w2 + "\n"

    print(s)


def check_available(seat_type):
    """
    returns true iff the pointer is less than number of seats of relevant type
    """
    return pointer[seat_type] < rows*2

def assign_seat(plane, name, seat_type):
    """
    replaces seat in plane with name of passengers
    increments pointer for seat type
    """
    plane[seat_type][pointer[seat_type]] = name
    pointer[seat_type] += 1

def purchase_seats(plane, name, seat_type):
    """
    checks availability. If available, assigns seat. Else asks purchaser
    to pick another seat type.
    """
    if check_available(seat_type):
        print("Your seat is available!")
        assign_seat(plane, name, seat_type)

    else:
        print("There are no more " + seat_type + " seats left. Choose a new type of seat.")
        seat_type = input("Which seat type would you prefer (window, aisle, middle)? ")
        purchase_seats(plane, name, seat_type)

pl = create_plane(rows)
print("before assigning seats:")

print_plane(pl)


for i in range(3):
    name = input("Enter your name: ")
    seat_type = input("Which seat type would you prefer (window, aisle, middle)? ")
    purchase_seats(pl, name, seat_type)
    print_plane(pl)
