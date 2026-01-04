import re
from grafana_series1_week5.client import call_inventory_api

# W3C Regex: version(2)-traceid(32)-spanid(16)-flags(2)
W3C_TRACEPARENT_RE = re.compile(r"^00-[a-f0-9]{32}-[a-f0-9]{16}-[a-f0-9]{2}$")


def test_trace_header_propagation_success(validate_o11y_headers):
    """
    SCENARIO: Happy Path.
    The dev correctly passed the trace_id.
    RESULT: The contract is honored.
    """
    mock_trace = "00-4bf92f3577b34da6a3ce929d0e0e4736-00f067aa0ba902b7-01"

    validate_o11y_headers.add("GET", "http://inventory/api/v1/item-123", status=200)

    call_inventory_api("item-123", trace_id=mock_trace)

    sent_headers = validate_o11y_headers.calls[0].request.headers
    assert sent_headers.get("traceparent") == mock_trace


def test_trace_header_missing_fails_build(validate_o11y_headers):
    """
    SCENARIO: The 'Fragile Chain' Snaps.
    A dev calls the API but forgets the trace_id (None).
    RESULT: The build MUST fail to prevent a production blind spot.
    """
    validate_o11y_headers.add("GET", "http://inventory/api/v1/item-123", status=200)

    # Action: We simulate the mistake (passing None or empty)
    call_inventory_api("item-123", trace_id=None)  # type: ignore

    sent_headers = validate_o11y_headers.calls[0].request.headers

    # 🛑 THIS IS THE SAFETY NET
    # If this assertion fails, the GitHub Action goes RED.
    assert "traceparent" in sent_headers, (
        "FATAL: Trace context lost! CI must block this PR."
    )


def test_trace_integrity_contract(validate_o11y_headers):
    """
    HOT PATH TEST: Ensures the 'Fragile Chain' isn't just present,
    but compliant with W3C standards.
    """
    mock_trace_id = "4bf92f3577b34da6a3ce929d0e0e4736"
    validate_o11y_headers.add("GET", re.compile(r".*"), status=200)

    # Action
    call_inventory_api("sg-item-88", trace_id=mock_trace_id)

    # Analysis
    sent_headers = validate_o11y_headers.calls[0].request.headers
    tp_header = sent_headers.get("traceparent", "")

    # 🛑 The Hardcore Check: Is it a valid W3C header?
    assert W3C_TRACEPARENT_RE.match(tp_header), (
        f"CRITICAL: Invalid traceparent format: '{tp_header}'. "
        "This will break Grafana Tempo visualization!"
    )

    # Ensure our trace_id is actually inside that header
    assert mock_trace_id in tp_header, "Trace ID mismatch!"
