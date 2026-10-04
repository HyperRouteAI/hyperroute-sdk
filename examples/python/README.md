# Python examples

Install with `pip install ./python` from the repository root.
Set `HYPERROUTE_API_KEY` for authenticated operations.

- [`recommend.py`](recommend.py): Requests the default lean response and prints every returned field. [Output](output/recommend.md).
- [`evidence.py`](evidence.py): Requests `detail="full"` with `evidence_k=3` and prints every returned field, including scores, facets, probe evidence, and judgments. [Output](output/evidence.md).
- [`minimal.py`](minimal.py): Requests `detail="min"` and prints the complete minimal response. [Output](output/minimal.md).
- [`text.py`](text.py): Requests `format="text"` and prints the complete text response. [Output](output/text.md).
- [`async_recommend.py`](async_recommend.py): Requests a recommendation asynchronously and prints the complete response. [Output](output/async_recommend.md).
- [`poll.py`](poll.py): Submits a recommendation job, waits for completion, and prints the complete recommendation. [Output](output/poll.md).
- [`stream.py`](stream.py): Prints each event name and its complete data as it arrives. [Output](output/stream.md).
- [`execute.py`](execute.py): Runs the specified tool and prints the complete execution response. This output shows a tool requiring a connected credential. [Output](output/execute.md).
- [`feedback.py`](feedback.py): Reports a tool outcome and prints the complete feedback response. [Output](output/feedback.md).
