from importlib import reload
import re
import verify

reload(verify)
from verify import VerifyStep  # noqa: E402

inserted_rx = re.compile(r"Inserted\s+(\d+)\s+diodes")


def handle(step, caplog):
    in_diodes = 35  # 102 input bits - disconnected (32 irq - 32 pcpi_rd - 1 pcpi_ready - 1 pcpi_wait - 1 pcpi_wr)
    out_diodes = 307  # 307 output bits, untouched
    expected_diodes = 0
    if step.config["DIODE_ON_PORTS"] in ["in", "both"]:
        expected_diodes += in_diodes
    if step.config["DIODE_ON_PORTS"] in ["out", "both"]:
        expected_diodes += out_diodes
    result = inserted_rx.search(caplog.text)
    got_diodes = int(result[1]) if result is not None else 0
    assert expected_diodes == got_diodes, "Inserted an unexpected number of diodes"
    step = VerifyStep(step.config, step.state_out)
    step.start(step_dir=".")
