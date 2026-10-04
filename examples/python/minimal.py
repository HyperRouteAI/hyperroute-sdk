import json
from hyperroute import HyperRoute

with HyperRoute() as client:
    response = client.recommend({
        'query': 'Find recent research on battery recycling',
        'detail': 'min',
    })
    print(json.dumps(response.data, indent=2, ensure_ascii=False))
