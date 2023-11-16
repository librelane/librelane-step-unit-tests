import os
import json
from openlane.steps.checker import TrDRC


def handle(step):
    assert (
        step.state_out.metrics[TrDRC.metric_name] == 0
    ), "DRC violations produced by detailed router"

    json_stats = f"{os.path.splitext(step.get_log_path())[0]}.process_stats.json"
    stats = {}
    with open(json_stats, "r") as f:
        stats = json.load(f)
    assert (
        stats["peak_resources"]["threads"] >= step.config["DRT_THREADS"] * 2
    ), f"DRT_THREADS set to {step.config['DRT_THREADS']}. Usage recorded: {stats['peak_resources']['threads']}"
