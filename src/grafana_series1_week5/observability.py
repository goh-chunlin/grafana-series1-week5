"""
The O11y Contract: Centralizing our metadata standards.
If it's not defined here, it doesn't exist in our traces.
"""

# Standard OTel Header
TRACE_HEADER = "traceparent"

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

    return {
        TRACE_HEADER: trace_id,
        SERVICE_VERSION_HEADER: CURRENT_VERSION
    }