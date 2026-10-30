import { parseArgs } from 'node:util';
import { HyperRoute } from '@hyperroute/sdk';
const { values, positionals } = parseArgs({ allowPositionals: true, options: { report: { type: 'string', multiple: true } } });
if (!positionals.length) throw new Error('Supply one or more queries and optionally --report ITEM=SCORE');
const reports = (values.report ?? []).map((r) => { const [item, score] = r.split('='); return { item, score }; });
const client = new HyperRoute();
console.log(JSON.stringify((await client.run({ items: positionals.map((query) => ({ query })), reports })).data, null, 2));
