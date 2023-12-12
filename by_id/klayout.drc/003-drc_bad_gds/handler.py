from openlane.steps import StepError


def handle(exception: StepError, caplog):
    assert exception is not None, "Malformed GDS did not raise an error"
    assert (
        "Stream has unknown format" in caplog.text
    ), "Did not handle malformed GDS correctly"
