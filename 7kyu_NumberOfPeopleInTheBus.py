def number(bus_stops):
    count = 0
    for stop in bus_stops:
        count += stop[0]
        count -= stop[1]
    return count


def number(bus_stops):
    count = 0
    for stop in bus_stops:
        for i, change in enumerate(stop):
            if i == 0:
                count += change
            else:
                count -= change

    return count