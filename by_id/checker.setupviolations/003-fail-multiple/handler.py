def handle(exception, caplog):
    assert exception is not None, "Checker didn't catch hold violations"
    print(caplog.text)

    bad_corners = ["min_tt_025C_1v80", "nom_tt_025C_1v80", "max_tt_025C_1v80"]
    for corner in bad_corners:
        assert corner in str(exception), f"Didn't catch {corner} corner"
