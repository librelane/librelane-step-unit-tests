def handle(step, exception):
    error_message = "Error encountered during running Magic"
    assert error_message in str(
        exception
    ), f"Different error raised.\nExpected: {error_message}\nFound: {str(exception)}"
