def handle(step, exception):
    from librelane.scripts.odbpy.exception_codes import NOT_FOUND_ERROR
    from librelane.steps.step import StepError

    assert (
        type(exception) == StepError
    ), "StepError not thrown. Probably something went very wrong"
    assert (
        exception.underlying_error
    ), "Underlying error not defined. Probably something went very wrong"
    assert (
        exception.underlying_error.args[0] == NOT_FOUND_ERROR
    ), "Different exception caught"
