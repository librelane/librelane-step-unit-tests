def handle(step, exception, caplog, openroad_alerts):
    assert exception is not None, "Detalied router didn't raise an exception"
    # [ERROR DRT-0155] Guide in net _000_ uses layer met1 (4) that is outside the allowed routing range
    error = "DRT-0155"
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
