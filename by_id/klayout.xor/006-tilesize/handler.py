import os
import subprocess


def handle(step):
    result = subprocess.call(
        [
            "grep",
            f"{step.config['KLAYOUT_XOR_TILE_SIZE']} µm",
            os.path.join(step.step_dir, "klayout-xor.log"),
        ],
    )
    assert result == 0, "could not set tile size properly"
