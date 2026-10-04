from hyperroute import HyperRoute

with HyperRoute() as client:
    response = client.recommend({
        'query': 'Find recent research on battery recycling',
        'format': 'text',
    })
    print(response.data)
