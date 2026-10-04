from typing import assert_type
from hyperroute import HyperRoute, AsyncHyperRoute, ApiResponse
from hyperroute.types import FullRecommendation, LeanRecommendation, MinRecommendation, Probe

client = HyperRoute()
assert_type(client.recommend({'query':'research'}), ApiResponse[LeanRecommendation])
assert_type(client.recommend({'query':'research','detail':'full'}), ApiResponse[FullRecommendation])
assert_type(client.recommend({'query':'research','detail':'min'}), ApiResponse[MinRecommendation])
assert_type(client.recommend({'query':'research','format':'text'}), ApiResponse[str])
full = client.recommend({'query':'research','detail':'full'}).data
if full['best'] is not None:
    assert_type(full['best']['capability'], float | None)
    if full['best']['evidence'] is not None:
        assert_type(full['best']['evidence']['probes'], list[Probe])

async def check_async() -> None:
    async with AsyncHyperRoute() as client:
        assert_type(await client.recommend({'query':'research','detail':'full'}), ApiResponse[FullRecommendation])
