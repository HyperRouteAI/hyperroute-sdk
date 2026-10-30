import { parseArgs } from 'node:util';
import { HyperRoute } from '@hyperroute/sdk';
const { values } = parseArgs({ options: { run: { type: 'string' }, item: { type: 'string' } } });
if (!values.run || !values.item) throw new Error('Supply --run RUN --item N');
const client = new HyperRoute();
console.log((await client.ranking({ run: values.run, item: Number(values.item) })).data);
