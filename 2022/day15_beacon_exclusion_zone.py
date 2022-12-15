import re


with open("inputs/day15.txt") as f:
    positions = [tuple(map(int, re.findall('-?\d+', line))) for line in f.read().splitlines()]


def get_intervals_covered_by_sensor(positions: list[tuple[int, int, int, int]], x_bound: int, y_coord: int) -> list[tuple[int, int]]:
    '''Returns the intervals covered by the sensor on horizonal line y at y=y_coord'''
    intervals_covered = []

    for sensor_x, sensor_y, beacon_x, beacon_y in positions:
        manhattan_distance = abs(sensor_x-beacon_x) + abs(sensor_y-beacon_y)
        y_diff = abs(sensor_y-y_coord)
        remaining = manhattan_distance - y_diff
        if remaining >= 0: intervals_covered.append([min(x_bound, sensor_x-remaining), min(x_bound, sensor_x+remaining)])

    return intervals_covered  


def merge_overlapping_intervals(intervals: list[tuple[int, int]]) -> list[tuple[int, int]]:
    without_overlaps = [[float("-inf"), float("-inf")]]

    for left, right in sorted(intervals):
        if left > without_overlaps[-1][1]: without_overlaps.append([left, right])
        else: without_overlaps[-1][1] = max(right, without_overlaps[-1][1])
    
    return without_overlaps[1:]


def get_num_points_covered(intervals: list[tuple[int, int]]) -> int:
    return sum(right-left for left, right in merge_overlapping_intervals(intervals))


def get_gap_in_interval(intervals: list[tuple[int, int]]) -> int | None:
    without_overlaps = merge_overlapping_intervals(intervals)
    if len(without_overlaps) == 1: return None
    return without_overlaps.pop()[0] - 1


def part1(positions: list[tuple[int, int, int, int]], y_coord: int) -> int:
    intervals = get_intervals_covered_by_sensor(positions=positions, y_coord=y_coord, x_bound=float("inf"))
    return get_num_points_covered(intervals=intervals)


def part2(positions: list[tuple[int, int, int, int]], x_bound: int, y_bound: int) -> int:
    for y in range(y_bound):
        intervals = get_intervals_covered_by_sensor(positions=positions, y_coord=y, x_bound=x_bound)
        x = get_gap_in_interval(intervals=intervals)
        if x is not None: return x * x_bound + y


if __name__=="__main__":
    print(part1(positions=positions, y_coord=2_000_000))
    print(part2(positions=positions, x_bound=4_000_000, y_bound=4_000_000))