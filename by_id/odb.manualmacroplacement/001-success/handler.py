import subprocess
import json
from openlane.common import GenericDictEncoder


def handle(step):
    subprocess.check_call(
        [
            "openroad",
            "-exit",
            "-python",
            "verify-odb.py",
            step.state_out["odb"],
            json.dumps(step.config["MACROS"]["spm"], cls=GenericDictEncoder),
        ]
    )
