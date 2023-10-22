def handle(step, exception):
    from openlane.scripts.odbpy.exception_codes import FORMAT_ERROR
    from openlane.steps.step import StepError

    assert (
        type(exception) == StepError
    ), "StepError not thrown. Probably something went very wrong"
    assert (
        exception.underlying_error
    ), "Underlying error not defined. Probably something went very wrong"
    assert (
        exception.underlying_error.args[0] == FORMAT_ERROR
    ), "Different exception caught"
