with open("inputs/day02.txt") as f:
    shape_score = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    player_picks = [
        (shape_score[player_one_pick], shape_score[player_two_pick]) 
        for player_one_pick, _, player_two_pick in f.read().splitlines()
    ]


def part1(player_picks: list[str]) -> int:
    return sum(
        player_two_pick + 3 * ((player_two_pick-player_one_pick+1) % 3)
        for player_one_pick, player_two_pick in player_picks
    )


def part2(player_picks: list[str]) -> int:
    return sum(
        (player_one_pick+player_two_pick) % 3 + 1 + (player_two_pick-1) * 3
        for player_one_pick, player_two_pick in player_picks
    )


if __name__=='__main__':
    # print(part1(player_picks))
    print(part2(player_picks))