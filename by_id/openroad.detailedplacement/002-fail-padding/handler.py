from librelane.steps import StepError


def handle(exception: StepError, caplog, openroad_alerts):
    assert exception is not None, "Util > 100% did not raise detailed placement error."
    alert_code = "DPL-0011"
    assert alert_code in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {alert_code} found"
