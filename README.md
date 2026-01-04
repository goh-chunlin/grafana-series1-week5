## ⚔️ Quest: Protect the Fragile Chain

The Context: Our SRE team is blind because traces are dropping. The Mission: > 1. Install dependencies: poetry install 2. Run the test: poetry run pytest 3. The Sabotage: Open client.py, delete the headers argument in the requests.get call, and run the test again. 4. The Result: Watch the build fail. That failure just saved you a 3:00 AM production call.

The Problem: Your junior dev just "optimized" the network client and accidentally deleted the tracing headers. The Consequence: Your $10k/month Grafana dashboard now shows "No Data."

Your Mission:

Setup: poetry install

Run Tests: poetry run pytest (Observe the green ✅)

The Sabotage: Open src/order_service/client.py and comment out the headers in the requests.get call.

The Verify: Run poetry run pytest again. Watch the build go RED.

Lesson: If the traceparent doesn't travel, the trace dies.