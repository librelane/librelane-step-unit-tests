from verify import VerifyStep


def handle(step):
    step = VerifyStep(step.config, step.state_out)
    step.start(step_dir=".")
