def handle(step, exception, caplog, openroad_alerts):
    assert exception is not None, "Didn't fail on negative core margin"
    error = "STA-0572"
    print(openroad_alerts)
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
