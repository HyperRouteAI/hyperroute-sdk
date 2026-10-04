import { HyperRoute } from '@hyperroute/sdk';
const client = new HyperRoute();
for await (const event of client.streamRecommendation({ query: 'Find recent research on battery recycling' })) {
  console.log(JSON.stringify({ event: event.event, data: event.data }, null, 2));
}
