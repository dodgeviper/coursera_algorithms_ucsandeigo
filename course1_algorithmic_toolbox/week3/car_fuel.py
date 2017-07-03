"""
Distance with full tank = x km.
Find the minimum number of refills to get from Point A to point B.

Input:
A car which can travel at most L kilometers with full tank, a source
point A, a destination point B and n gas stations at distances x1<= x2 <= x3..<= xn
in kilometers from A along with path from A to B.

Output:
Minimum number of refills required to travel from A to B.
"""

def greedy_strategy(max_distance_with_full_tank, source_a, dest_b, gas_stations):
    """
    :param max_distance_with_full_tank:
    :param source_a:
    :param dest_b:
    :param gas_stations: list of integers contains gas stations located at distance markers
    from A. This list is ordered.
    :return:
    """
    start = 0
    pit_stops = []
    refills = 0
    # Find local maximum points of gas stations which can cover the max distance on full tank.
    previous = 0
    for station in gas_stations:
        if (max_distance_with_full_tank * (refills + 1)) < station:
            if (station - previous) > max_distance_with_full_tank:
                return "Not possible, get a bigger fuel tank"
            pit_stops.append(previous)
            refills += 1
        previous = station
    return pit_stops, refills


print(greedy_strategy(400, 0, 950, [200, 375, 550, 750, 950]))

print(greedy_strategy(400, 0, 950, [100, 550, 750, 950]))

