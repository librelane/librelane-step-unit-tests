def handle(step, exception, caplog, openroad_alerts):
    assert exception is not None, "Detalied router didn't raise an exception"
    print(openroad_alerts)
    # [ERROR DRT-0218] Guide is not connected to design
    error = "DRT-0218"
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
