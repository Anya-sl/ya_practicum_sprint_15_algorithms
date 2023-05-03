# 86613038
from typing import List


def get_dist_to_neighbours(street_row: List[int]) -> List[int]:
    street_len = len(street_row)
    dist = [0] * street_len
    zero_indexes = [
        index for index in range(street_len) if street_row[index] == 0]

    for index in range(zero_indexes[0]):
        dist[index] = zero_indexes[0] - index
    for index in range(len(zero_indexes) - 1):
        for sub_index in range(zero_indexes[index] + 1,
                               zero_indexes[index + 1]):
            dist[sub_index] = min(sub_index - zero_indexes[index],
                                  zero_indexes[index+1] - sub_index)
    for index in range(zero_indexes[-1] + 1, street_len):
        dist[index] = index - zero_indexes[-1]

    return dist


if __name__ == '__main__':
    _ = int(input())
    street_row = list(map(int, input().strip().split()))
    print(*get_dist_to_neighbours(street_row))
