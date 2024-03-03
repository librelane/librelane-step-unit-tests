def handle(step, exception, caplog):
    assert exception is None, "Didn't expect an errors to be thrown by OpenLane"
    correct_corners = ["min_ss_100C_1v60", "min_ff_n40C_1v95"]
    warn_corners = [
        "nom_ff_n40C_1v95",
        "nom_tt_025C_1v80",
        "max_tt_025C_1v80",
        "nom_ss_100C_1v60",
        "max_ss_100C_1v60",
        "max_ff_n40C_1v95",
        "min_tt_025C_1v80",
    ]
    for corner in warn_corners:
        assert corner in caplog.text, f"Didn't warn about {corner}"
    for corner in correct_corners:
        assert (
            corner not in caplog.text
        ), f"Warning generated about {corner} when there shouldn't have been any."
