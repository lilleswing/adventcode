import sys
import requests

def main(day, cookie):
    url = f"https://adventofcode.com/2024/day/{day}/input"
    headers = {
        "cookie": f"session={cookie}"
    }
    response = requests.get(url, headers=headers)
    if len(str(day)) == 1:
        day = f"0{day}"
    if response.status_code != 200:
        print(f"Failed to get input data for day {day}")
        raise ValueError("Failed to get input data")
    with open(f"day{day}.in", "w") as f:
        f.write(response.text)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
