def handle(step, exception, caplog, openroad_alerts):
    assert exception is None, "A pin missing from the design raised an exception"
    assert "not found in design but found in config" in ";".join(
        alert.message for alert in openroad_alerts
    ), "no message printed about missing pin"
