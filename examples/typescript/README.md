# TypeScript and JavaScript examples

Build with `npm --prefix typescript ci && npm --prefix typescript run build` from the repository root, then run `npm --prefix examples/typescript install`.
Set `HYPERROUTE_API_KEY` for authenticated operations.

- [`recommend.mjs`](recommend.mjs): Requests the default lean response and prints every returned field. [Output](output/recommend.md).
- [`evidence.mjs`](evidence.mjs): Requests `detail="full"` with `evidence_k=3` and prints every returned field, including scores, facets, probe evidence, and judgments. [Output](output/evidence.md).
- [`minimal.mjs`](minimal.mjs): Requests `detail="min"` and prints the complete minimal response. [Output](output/minimal.md).
- [`text.mjs`](text.mjs): Requests `format="text"` and prints the complete text response. [Output](output/text.md).
- [`poll.mjs`](poll.mjs): Submits a recommendation job, waits for completion, and prints the complete recommendation. [Output](output/poll.md).
- [`stream.mjs`](stream.mjs): Prints each event name and its complete data as it arrives. [Output](output/stream.md).
- [`execute.mjs`](execute.mjs): Runs the specified tool and prints the complete execution response. This output shows a tool requiring a connected credential. [Output](output/execute.md).
- [`feedback.mjs`](feedback.mjs): Reports a tool outcome and prints the complete feedback response. [Output](output/feedback.md).
