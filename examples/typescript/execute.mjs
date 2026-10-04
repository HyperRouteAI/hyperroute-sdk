import { parseArgs } from 'node:util';
import { HyperRoute } from '@hyperroute/sdk';
const { values } = parseArgs({ options: { execute: { type: 'boolean' }, 'tool-id': { type: 'string' }, 'session-id': { type: 'string' }, query: { type: 'string' } } });
if (!values.execute || !values['tool-id'] || !values.query) throw new Error('Supply --execute --tool-id TOOL --query QUERY and optionally --session-id SESSION');
const client = new HyperRoute();
console.log(JSON.stringify((await client.execute({ tool_id: values['tool-id'], query: values.query, session_id: values['session-id'] })).data, null, 2));
