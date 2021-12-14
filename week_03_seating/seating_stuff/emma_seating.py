# Create a dictionary (keys + count) to count passengers who want [window, middle, aisle] seats

seats_requested = {
  "window": 0,
  "middle": 0,
  "aisle": 0
}

def create_plane(rows):
    """
    A list of 3 row*2-length lists, representing window, aisle, middle seats.
    """
    window = ["window"]*rows*2
    middle = ["middle"]*rows*2
    aisle = ["aisle"]*rows*2
    plane = [window, middle, aisle]
    """
    for r in range(rows):
        s = ["window"]+["middle"]+["aisle"]+["aisle"]+["middle"]+["window"]
        plane.append(s)
    """
    return plane

def get_plane_string(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: a string suitable for printing.
    """
    s = ""
    for r in plane:
        r = ["%10s"%x for x in r] # This is a list comprehension - an advanced Python feature
        s = s + " ".join(r)
        s = s + "\n"
    return s

def get_total_seats(plane):
    """
    Params: plane : a list of lists representing a plane
    Returns: The total number of seats in the plane
    """
    return len(plane)*len(plane[0])

def fill_plane(plane):
    """
    Params: plane - a list of lists representing a plane
    comments interspersed in the code
    """
    seats_sold={}
    total_seats = get_total_seats(plane)

    return plane

def get_number_seats_sold(seats_requested):
    """
Input: a dictionary containing the number of regular economy seats sold.
           the keys are the names for the tickets and the values are how many
    ex:   {'Robinson':3, 'Lee':2 } // The Robinson family reserved 3 seats, the Lee family 2
    Returns: the total number of seats sold
    """
    sold = 0
    for v in seats_requested.values():
        sold = sold + v
    return sold

def get_avail_seats(plane,seats_sold):
    """
    Parameters: plane : a list of lists representing plaine
                economy_sold : a dictionary of the economy seats sold but not necessarily assigned
    Returns: the number of unsold seats
    Notes: this loops over the plane and counts the number of seats that are "avail" or "win"
           and removes the number of economy_sold seats
    """
    avail = 0;
    for r in plane:
        for c in r:
            if c == "win" or c == "middle" or c == "aisle":
                avail = avail + 1
    avail = avail - get_number_seats_sold(seats_requested)
    return avail



# This function is very similar to the original purchase_economy_plus function
# But it also takes in what type of seat a user would like
def purchase_seats(plane, name, seat_type):
    """
    Params: plane - a list of lists representing a plane
            name - the name of the person purchasing the seat
            seat_type - window, middle, or aisle
    """
    rows = len(plane)
    cols = len(plane[0])

    # total unassigned seats
    seats = get_avail_seats(plane,seats_sold)
    print("seats left = ", seats)

    # exit if we have no more seats
    if seats < 1:
        return plane

    # Increment the type of seat requested and update the dictionary
    if seat_type == "window":
        seats_requested["window"] += 1

    elif seat_type == "middle":
        seats_requested["middle"] += 1

    elif seat_type == "aisle":
        seats_requested["aisle"] += 1

# function to fill the least requested seats first
def assign_seats(seats_requested):

    # Find the least requested type of seat
    least_requested = min(seats_requested)

    # Assign the least requested seats first
    # Then remove those from the dictionary

    print("least requested = ", least_requested)

    return least_requested


def main():
    plane = create_plane(5)
    print(get_plane_string(plane))
    print(seats_requested)
    plane = fill_plane(plane)
    print(get_plane_string(plane))

    purchase_seats(plane,seats_requested,"Smith","window")
    purchase_seats(plane,seats_requested,"Doe","aisle")
    purchase_seats(plane,seats_requested,"Roberts","middle")
    purchase_seats(plane,seats_requested,"Green","window")
    purchase_seats(plane,seats_requested,"Brown","window")
    purchase_seats(plane,seats_requested,"Stone","middle")
    print(seats_requested)

    assign_seats(seats_requested)

if __name__=="__main__":
    main()
