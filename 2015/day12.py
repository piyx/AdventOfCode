import json
import re


with open('inputs/12', 'r') as f:
    data = json.loads(f.read().strip())


def solve(data):
    if type(data) == str: return 0
    elif type(data) == int: return data
    elif type(data) == list: return sum(solve(item) for item in data)
    else: return "red" not in data.values() and sum(solve(item) for item in data.values())
    

if __name__ == "__main__":
    print(sum(map(int, re.findall(r'\d+|-\d+', str(data)))))
    print(solve(data))
    
