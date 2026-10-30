import argparse
from hyperroute import HyperRoute

parser = argparse.ArgumentParser()
parser.add_argument('--run', required=True)
parser.add_argument('--item', type=int, required=True)
args = parser.parse_args()

with HyperRoute() as client:
    print(client.ranking({'run': args.run, 'item': args.item}).data)
