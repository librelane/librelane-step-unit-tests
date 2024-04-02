from openlane.steps import StepError


def handle(exception: StepError, caplog, openroad_alerts):
    assert exception is not None, "Util > 100% did not raise detailed placement error."
    error = "DPL-0036"
    assert error in [
        alert.code for alert in openroad_alerts
    ], f"No alerts for {error} found"
