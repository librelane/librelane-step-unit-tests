def handle(exception, caplog):
    assert exception is not None, "Checker didn't catch hold violations"
    print(caplog.text)
    assert "nom_tt_025C_1v80" in str(exception), "Didn't catch correct corner"
