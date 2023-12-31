def handle(exception, caplog):
    assert exception is not None, "Checker didn't catch hold violations"
    print(caplog.text)
    assert "nom_ss_100C_1v60" in str(exception), "Didn't catch correct corner"
