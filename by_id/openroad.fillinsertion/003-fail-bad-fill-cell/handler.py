def handle(step, exception, caplog, openroad_alerts):
    assert (
        exception is not None
    ), "Fill insertion didn't fail on bad fill cell defintion"
    error = "DPL-0002"
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
