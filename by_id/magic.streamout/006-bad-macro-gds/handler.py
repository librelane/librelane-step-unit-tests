def handle(step, exception):
    error_message = "Failed to extract PR boundary from GDSII view of macro"
    assert error_message in str(
        exception
    ), f"Different error raised: -'{error_message}' +'{str(exception)}'"
