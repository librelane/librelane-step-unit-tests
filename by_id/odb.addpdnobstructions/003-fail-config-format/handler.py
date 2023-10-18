def handle(step, exception):
    from openlane.scripts.odbpy.exception_codes import FORMAT_ERROR
    assert exception.args[0] == FORMAT_ERROR, f"Different exception caught"
