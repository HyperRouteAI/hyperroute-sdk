import json
import argparse
from hyperroute import HyperRoute

parser = argparse.ArgumentParser()
parser.add_argument('queries', nargs='+')
parser.add_argument('--report', nargs=2, metavar=('ITEM', 'SCORE'), action='append', default=[])
args = parser.parse_args()

with HyperRoute() as client:
    response = client.run({'items': [{'query': q} for q in args.queries],
                           'reports': [{'item': item, 'score': score} for item, score in args.report]})
    print(json.dumps(response.data, indent=2, ensure_ascii=False))
