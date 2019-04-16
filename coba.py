import argparse

ap = argparse.ArgumentParser()

ap.add_argument("-c", "--call", type=int, default=1)
ap.add_argument("-d", "--doll", type=int, default=0)

parser = ap.parse_args()

print(parser.call, parser.doll)
# print(parser.d)