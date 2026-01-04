import re
import secrets

"""
The O11y Contract: Centralizing our metadata standards.
If it's not defined here, it doesn't exist in our traces.
"""

# Standard OTel Header
TRACE_HEADER = "traceparent"
W3C_TRACEPARENT_RE = re.compile(r"^00-[a-f0-9]{32}-[a-f0-9]{16}-[a-f0-9]{2}$")

# Business-critical metadata for filtering in Grafana/Tempo
SERVICE_VERSION_HEADER = "service-version"
CURRENT_VERSION = "1.4.2"


def inject_o11y_headers(trace_id: str) -> dict:
    """
    Standardizes how headers are injected into outgoing requests.
    Prevents 'The Fragile Chain' from snapping due to manual typos.
    """
    if not trace_id:
        # In production, we might log a warning here
        # because an orphan span is about to be created.
        # However, for the sake of this exercise, we return an empty dict.
        return {}

    # To make this works with the existing tests, we need to ensure
    # that the trace_id is in W3C format.
    # You need to uncomment the following lines to enforce W3C formatting.
    # After that, you need to comment out the if not trace_id check above.

    # if not trace_id:
    #     trace_id = secrets.token_hex(16)
    # if not W3C_TRACEPARENT_RE.match(trace_id):
    #     # It's not a valid header, so we treat it as a raw Trace ID
    #     # and wrap it in the W3C envelope.
    #     # Ensure trace_id is exactly 32 chars (pad with 0 or trim)
    #     trace_id = trace_id.ljust(32, "0")[:32]
    #     span_id = secrets.token_hex(8)
    #     trace_id = f"00-{trace_id}-{span_id}-01"

    return {TRACE_HEADER: trace_id, SERVICE_VERSION_HEADER: CURRENT_VERSION}
