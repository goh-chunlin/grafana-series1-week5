## ⚔️ Quest: Protect the Fragile Chain

### The Context
Our SRE team is blind because traces are dropping. Your junior dev just "optimised" the network client and accidentally deleted the tracing headers. 

### The Consequence

Your Grafana dashboard now shows "No Data."

### Your Mission:

- Setup: `poetry install`
- Run Tests: `poetry run pytest` (Observe the fails)
- The Sabotage: Open `src/grafana_series1_week5/observability.py` and uncomment the logic to:
    1. Generate a new trace ID if one is missing.
    2. Enforce W3C Trace Context standards (using Regex validation).
- The Verify: Run `poetry run pytest` again. Watch the build go GREEN.

### Lesson

If the traceparent does NOT travel, the trace dies. And if it travels in the wrong format (e.g. "123"), the collector will kill it.

