def handle(step, exception, caplog, openroad_alerts):
    assert exception is not None, "Didn't fail on unknown metal layer"
    error = "PPL-0051"
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
