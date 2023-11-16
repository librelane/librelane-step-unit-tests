from openlane.steps import StepError


def handle(exception: StepError, caplog):
    error_msg = "[ERROR DPL-0036] Detailed placement failed."
    assert exception is not None, "Util > 100% did not raise detailed placement error."
    assert error_msg in caplog.text, f"{error_msg} not found in log file"
