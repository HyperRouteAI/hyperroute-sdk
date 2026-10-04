import { HyperRoute } from '@hyperroute/sdk';
const client = new HyperRoute();
const { data } = await client.recommend({
  query: 'Find recent research on battery recycling',
  detail: 'full',
  evidence_k: 3,
});
console.log(JSON.stringify(data, null, 2));
