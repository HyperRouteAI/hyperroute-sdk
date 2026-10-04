import asyncio
import json
from hyperroute import AsyncHyperRoute

async def main():
    async with AsyncHyperRoute() as client:
        recommendation = (await client.recommend({'query': 'Find recent research on battery recycling'})).data
        print(json.dumps(recommendation, indent=2, ensure_ascii=False))

asyncio.run(main())
