import json
import argparse
from hyperroute import HyperRoute

parser = argparse.ArgumentParser()
parser.add_argument('--session-id', required=True)
parser.add_argument('--tool-id', required=True)
parser.add_argument('--score', required=True, choices=['full', 'partial', 'useless', 'not_used', 'blocked'])
args = parser.parse_args()

with HyperRoute() as client:
    print(json.dumps(client.report_outcome({'session_id': args.session_id, 'tool_id': args.tool_id, 'score': args.score}).data, indent=2, ensure_ascii=False))
