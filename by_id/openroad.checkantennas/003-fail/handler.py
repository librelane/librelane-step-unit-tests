def handle(step, exception, caplog, openroad_alerts):
    assert exception is not None, "Didn't fail on non routed design"

    error = "ANT-0008"
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
