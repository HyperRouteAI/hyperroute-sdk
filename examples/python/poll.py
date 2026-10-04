import json
from hyperroute import HyperRoute

with HyperRoute() as client:
    job = client.submit_recommendation({'query': 'Find recent research on battery recycling'})
    recommendation = client.wait_for_recommendation(job.data['job']).data
    print(json.dumps(recommendation, indent=2, ensure_ascii=False))
