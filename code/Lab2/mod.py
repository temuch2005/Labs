def days_to_exceed_distance(initial_distance, percent_increase):
    distance = initial_distance
    days = 1

    while distance <= 50:
        distance += distance * (percent_increase / 100)
        days += 1

    return days
