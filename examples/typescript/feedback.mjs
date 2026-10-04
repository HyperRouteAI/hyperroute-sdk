import { parseArgs } from 'node:util';
import { HyperRoute } from '@hyperroute/sdk';
const { values } = parseArgs({ options: { 'session-id': { type: 'string' }, 'tool-id': { type: 'string' }, score: { type: 'string' } } });
if (!values['session-id'] || !values['tool-id'] || !['full', 'partial', 'useless', 'not_used', 'blocked'].includes(values.score)) throw new Error('Supply --session-id SESSION --tool-id TOOL --score full|partial|useless|not_used|blocked');
const client = new HyperRoute();
console.log(JSON.stringify((await client.reportOutcome({ session_id: values['session-id'], tool_id: values['tool-id'], score: values.score })).data, null, 2));
