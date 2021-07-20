def flights(*args):
    valid_flights = []
    for el in args:
        if el == "Finish":
            break
        valid_flights.append(el)

    all_flights = {}
    for i in range(0, len(valid_flights), 2):
        if valid_flights[i] not in all_flights:
            all_flights[valid_flights[i]] = valid_flights[i + 1]
        else:
            all_flights[valid_flights[i]] += valid_flights[i + 1]

    return all_flights



print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))