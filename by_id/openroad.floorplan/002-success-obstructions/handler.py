from importlib import reload
import verify

reload(verify)
from verify import VerifyStep  # noqa: E402


def handle(step):
    step = VerifyStep(step.config, step.state_out)
    step.start(step_dir=".")
