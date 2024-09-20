import math

def distance(p1, p2):
    """Calculates the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def closest_pair(points):
    """Finds the closest pair of points using the divide-and-conquer algorithm."""

    def sort_by_x(points):
        return sorted(points, key=lambda p: p[0])

    def sort_by_y(points):
        return sorted(points, key=lambda p: p[1])

    def divide_and_conquer(points):
        n = len(points)
        if n <= 3:
            return min(distance(points[i], points[j]) for i in range(n) for j in range(i + 1, n))

        mid = n // 2
        left_points = points[:mid]
        right_points = points[mid:]

        delta_left = divide_and_conquer(left_points)
        delta_right = divide_and_conquer(right_points)
        delta = min(delta_left, delta_right)

        # Find points within delta of the dividing line
        mid_x = (left_points[-1][0] + right_points[0][0]) / 2
        strip = [p for p in points if abs(p[0] - mid_x) <= delta]

        # Sort strip points by y-coordinate
        strip = sort_by_y(strip)

        # Check distances within the strip
        for i in range(len(strip)):
            for j in range(i + 1, min(i + 7, len(strip))):
                if distance(strip[i], strip[j]) < delta:
                    delta = distance(strip[i], strip[j])

        return delta

    points = sort_by_x(points)
    return divide_and_conquer(points)

# Example usage
points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
closest_distance = closest_pair(points)
print("Closest distance:", closest_distance)