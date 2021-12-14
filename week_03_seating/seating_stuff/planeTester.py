#pointers will be Incremented as seats are purchased
pointer = {
"window":0,
"middle":0,
"aisle":0
}
rows = 10;
def create_plane(rows):
    """
    A list of 3 row*2-length lists, representing window, aisle, middle seats.
    """
    plane = {
        "window": ["window"]*rows*2,
        "middle": ["middle"]*rows*2,
        "aisle": ["aisle"]*rows*2
    }
    """
    window = ["window"]*rows*2
    middle = ["middle"]*rows*2
    aisle = ["aisle"]*rows*2
    plane = [window, middle, aisle]
    """

    """
    for r in range(rows):
        s = ["window"]+["middle"]+["aisle"]+["aisle"]+["middle"]+["window"]
        plane.append(s)
    """
    return plane

def print_plane(plane):
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
    returns a boolean if the pointer is less than number of seats
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
    if check_available(seat_type):
        print("Your seat is available!")
        assign_seat(plane, name, seat_type)

    else:
        print("There are no more " + seat_type + " seats left. Choose a new type of seat.")
        seat_type = input("Which seat type would you prefer (window, aisle, middle)? ")
        purchase_seats(plane, name, seat_type)

pl = create_plane(rows)
print("before assigning seats:")
#print(pl)


print_plane(pl)


for i in range(3):
    name = input("Enter your name: ")
    seat_type = input("Which seat type would you prefer (window, aisle, middle)? ")
    purchase_seats(pl, name, seat_type)
    print_plane(pl)
