def handle(step, caplog):
    assert (
        "Connecting power net vccd2 to mprj/VPWR" in caplog.text
    ), "Did not attempt to connect power net"
    assert (
        "Made 1 connections" in caplog.text
    ), "No connections appear to have been made"
