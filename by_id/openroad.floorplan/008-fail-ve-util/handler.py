def handle(step, exception, caplog, openroad_alerts):
    assert exception is not None, "Didn't fail on negative utilization"
    error = "IFP-0012"
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
