def add_flight(flights,flight_code, flight_duration, flight_departure,flight_destination):
    """Adds a flight to the list of flights"""
    try:
        flight_duration = int(flight_duration)
    except ValueError:
        return False
    if len(flight_code) < 3 or flight_duration < 20 or len(flight_departure) < 3 or len(flight_destination) < 3:
        return False
    else:
        flights.append([flight_code, int(flight_duration), flight_departure,flight_destination])
        return True

def delete_flight(flights, flight_code):
    """Deletes a flight from the list of flights"""
    for i in range(len(flights)):
        if flights[i][0] == flight_code:
            flights.pop(i)
            return True
    return False

#sorts the flights by destination
def sort_flights(flights):
    """Sorts the flights by destination"""
    for i in range(len(flights)):
        for j in range(len(flights)):
            if flights[i][3] < flights[j][3]:
                flights[i], flights[j] = flights[j], flights[i]

def validate_departure_minutes(flights, departure, minutes):
    """Validates the departure and minutes"""
    try:
        minutes = int(minutes)
    except ValueError:
        return False
    if minutes < 10 or minutes > 60:
        return False
    else:
        if len(departure) < 3:
            return False
        else:
            for i in range(len(flights)):
                if flights[i][2] == departure:
                    return True
            return False

def strong_winds(flights, departure, minutes):
    """Updates the flight duration of flights from a departure by adding the minutes to the flight duration"""
    for i in range(len(flights)):
        if flights[i][2] == departure:
            flights[i][1] = flights[i][1] + minutes

def test_add_flight():
    """Tests the add_flight function"""
    flights = []
    assert add_flight(flights, "ABC", 20, "ABC", "ABC") == True
    assert add_flight(flights, "ABC", 19, "ABC", "ABC") == False #invalid duration
    assert add_flight(flights, "", 20, "ABC", "ABC") == False    #invalid code
    assert add_flight(flights, "ABC", 20, "", "ABC") == False   #invalid departure
    assert add_flight(flights, "ABC", 20, "ABC", "") == False   #invalid destination

def test_delete_flight():
    """Tests the delete_flight function"""
    flights = [["ABC", 20, "ABC", "ABC"], ["CBA", 20, "ABC", "ABC"]]
    assert delete_flight(flights, "ABC") == True
    assert delete_flight(flights, "AAA") == False
    assert delete_flight(flights, "CBA") == True
    
def test_sort_flights():
    """Tests the sort_flights function"""
    flights = [["ABC", 20, "ABC", "ABC"], ["CBA", 20, "ABC", "ABC"], ["AAA", 20, "ABC", "AAA"]]
    sort_flights(flights)
    assert flights == [["AAA", 20, "ABC", "AAA"], ["ABC", 20, "ABC", "ABC"], ["CBA", 20, "ABC", "ABC"]]

def test_validate_departure_minutes():
    """Tests the validate_departure_minutes function"""
    flights = [["ABC", 20, "ABC", "ABC"], ["CBA", 20, "ABC", "ABC"], ["AAA", 20, "ABC", "AAA"]]
    assert validate_departure_minutes(flights, "ABC", 10) == True
    assert validate_departure_minutes(flights, "ABC", 9) == False #invalid minutes
    assert validate_departure_minutes(flights, "ABC", 61) == False #invalid minutes
    assert validate_departure_minutes(flights, "BBB", 10) == False #invalid departure

def test_strong_winds():
    """Tests the strong_winds function"""
    flights = [["ABC", 20, "ABC", "ABC"], ["CBA", 20, "ABC", "ABC"], ["AAA", 20, "ABC", "AAA"]]
    strong_winds(flights, "ABC", 10)
    assert flights == [["ABC", 30, "ABC", "ABC"], ["CBA", 30, "ABC", "ABC"], ["AAA", 20, "ABC", "AAA"]]