def handle(step, exception, caplog, openroad_alerts):
    warning = "GPL-0302"
    assert warning in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {warning} found"
