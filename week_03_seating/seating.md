It seems to me that what people are really buying with economy plus is
the higher probability of getting a window seat.  A simpler and more
equitable, or at least straightforward, algorithm would be to set aside
a limited number of window seats, to be sold at a higher price. After
those have been sold, the economy seats would be assigned randomly.  

The resulting algorithm will be pretty simple:

while totalSeats > 1:
  select random number r
  if r > 30 and windowSeats > 1:
    select window seat, replace with name of passenger
    decrement windowSeat
  else:
    select random non-window seat, replace with name of passenger
  decrement totalSeat 
