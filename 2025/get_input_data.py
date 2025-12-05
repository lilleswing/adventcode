import datetime
import os.path
import sys

import requests


def main(day, cookie):
    url = f"https://adventofcode.com/2025/day/{day}/input"
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
    print(response.text)

    sample_fname = f"day{day}.sample"
    if not os.path.exists(sample_fname):
        with open(sample_fname, "w") as f:
            f.write("")

    app_fname = f"day{day}.py"
    if not os.path.exists(app_fname):
        with open(app_fname, "w") as f:
            f.write("")


def read_cookie_from_env():
    lines = open('.env').readlines()
    for line in lines:
        if line.startswith('COOKIE='):
            return line.split('=')[1].strip()
    raise ValueError("Failed to read cookie from .env")


if __name__ == "__main__":
    args = list(sys.argv)
    if len(args) == 1:
        now = datetime.datetime.now()
        day_of_month = now.day
        args.append(str(day_of_month))
    if len(args) == 2:
        cookie = read_cookie_from_env()
        args.append(cookie)
    main(args[1], args[2])
