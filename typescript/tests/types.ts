import { HyperRoute, type FullRecommendation, type LeanRecommendation, type MinRecommendation, type Probe, type ApiResponse } from '../src/index.js';

const client = new HyperRoute();
const full: Promise<ApiResponse<FullRecommendation>> = client.recommend({ query: 'research', detail: 'full' });
const lean: Promise<ApiResponse<LeanRecommendation>> = client.recommend({ query: 'research' });
const min: Promise<ApiResponse<MinRecommendation>> = client.recommend({ query: 'research', detail: 'min' });
const text: Promise<ApiResponse<string>> = client.recommend({ query: 'research', format: 'text' });
async function inspect() {
  const { data } = await full;
  if (data.best) {
    const score: number | null = data.best.capability;
    const band: number | null = data.best.band;
    const facets = data.best.facets.map(f => [f.name, f.raw, f.contribution]);
    const probes: Probe[] = data.best.evidence?.probes ?? [];
    return { score, band, facets, probes };
  }
}
void [lean, min, text, inspect];
