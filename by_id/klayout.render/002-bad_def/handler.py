from openlane.steps import StepError


def handle(exception: StepError, caplog):
    assert exception is not None, "Malformed DEF did not raise an error"
    assert "Expected token:" in caplog.text, "Did not handle malformed DEF correctly"
