import { HyperRoute } from '@hyperroute/sdk';
const client = new HyperRoute();
const job = await client.submitRecommendation({ query: 'Find recent research on battery recycling' });
const { data } = await client.waitForRecommendation(job.data.job);
console.log(JSON.stringify(data, null, 2));
