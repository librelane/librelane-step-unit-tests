def handle(step, caplog):
    assert (
        "Connecting power net vccd2 to mprj/VPWR" in caplog.text
    ), "Did not attempt to connect power net"
    assert (
        "mprj/VPWR is already connected to vccd2" in caplog.text
    ), "Did not print message for already-connected net"
