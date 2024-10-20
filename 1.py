import heapq


def min_cost_to_connect_cables(cable_lengths):
    # Create a heap from the list of cable lengths
    heapq.heapify(cable_lengths)

    total_cost = 0

    # While more than one cable remains, continue connecting
    while len(cable_lengths) > 1:
        # Pop the two smallest cables
        first = heapq.heappop(cable_lengths)
        second = heapq.heappop(cable_lengths)

        # The cost to connect them is the sum of their lengths
        cost = first + second
        total_cost += cost

        # Push the combined cable back into the heap
        heapq.heappush(cable_lengths, cost)

    return total_cost


# Example usage:
cable_lengths = [5, 4, 2, 8, 15, 22]
print(min_cost_to_connect_cables(cable_lengths))