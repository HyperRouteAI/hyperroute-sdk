import json
from hyperroute import HyperRoute

with HyperRoute() as client:
    recommendation = client.recommend({'query': 'Find recent research on battery recycling'}).data
    print(json.dumps(recommendation, indent=2, ensure_ascii=False))
