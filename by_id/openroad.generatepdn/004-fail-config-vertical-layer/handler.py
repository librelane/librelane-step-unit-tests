def handle(step, exception, caplog, openroad_alerts):
    assert exception is not None, "Check nodes didn't catch missing PDN"
    error = "PDN-1023"
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
