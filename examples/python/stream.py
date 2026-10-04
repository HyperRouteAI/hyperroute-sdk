import json
from hyperroute import HyperRoute

with HyperRoute() as client:
    for event in client.stream_recommendation({'query': 'Find recent research on battery recycling'}):
        print(json.dumps({'event': event.event, 'data': event.data}, indent=2, ensure_ascii=False))
