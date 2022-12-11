with open("inputs/day06.txt") as f:
    datastream = f.read().strip()


def get_start_of_message_market(datastream: str, window_size: int) -> int:
    return next(
        idx for idx in range(len(datastream))
        if len(set(datastream[idx: idx+window_size])) == window_size
    )


if __name__=="__main__":
    print(get_start_of_message_market(datastream=datastream, window_size=4))
    print(get_start_of_message_market(datastream=datastream, window_size=14))