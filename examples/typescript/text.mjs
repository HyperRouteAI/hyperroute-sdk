import { HyperRoute } from '@hyperroute/sdk';
const client = new HyperRoute();
const { data } = await client.recommend({
  query: 'Find recent research on battery recycling',
  format: 'text',
});
console.log(data);
