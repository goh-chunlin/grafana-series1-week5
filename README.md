## ⚔️ Quest: Protect the Fragile Chain

### The Context
Our SRE team is blind because traces are dropping. Your junior dev just "optimised" the network client and accidentally deleted the tracing headers. 

### The Consequence

Your $10k/month Grafana dashboard now shows "No Data."

### Your Mission:

- Setup: `poetry install`
- Run Tests: `poetry run pytest` (Observe the fails)
- The Sabotage: Open `src/grafana-series1-week5/client.py` and add logic to generate a new trace ID if one is missing
- The Verify: Run `poetry run pytest` again. Watch the build go GREEN.

### Lesson

If the traceparent does NOT travel, the trace dies.
