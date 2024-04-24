def handle(step, exception, caplog, openroad_alerts):
    assert exception is not None, "Didn't fail on negative core margin"
    # [ERROR STA-0572] -core_space '-4.6000000000000005' is not a positive float
    error = "STA-0572"
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
