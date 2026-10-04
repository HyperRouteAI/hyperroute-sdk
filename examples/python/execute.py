import json
import argparse
from hyperroute import HyperRoute

parser = argparse.ArgumentParser()
parser.add_argument('--execute', action='store_true', required=True)
parser.add_argument('--tool-id', required=True)
parser.add_argument('--session-id')
parser.add_argument('--query', required=True)
args = parser.parse_args()

with HyperRoute() as client:
    response = client.execute({'tool_id': args.tool_id, 'query': args.query, 'session_id': args.session_id})
    print(json.dumps(response.data, indent=2, ensure_ascii=False))
