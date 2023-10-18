def handle(step, exception):
    from openlane.scripts.odbpy.exception_codes import METAL_LAYER_ERROR
    assert exception.args[0] == METAL_LAYER_ERROR, f"Different exception caught"
