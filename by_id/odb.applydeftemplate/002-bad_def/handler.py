from openlane.steps import StepError


def handle(exception: StepError, caplog):
    assert exception is not None, "Malformed DEF did not raise an error"
    print("caplog says:")
    print(caplog.text)
    assert (
        "Def parser has encountered an error" in caplog.text
    ), "Did not handle malformed DEF correctly"
