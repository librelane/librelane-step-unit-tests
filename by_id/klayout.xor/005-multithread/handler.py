import os
import json


def handle(step):
    stat_path = os.path.join(step.step_dir, "klayout-xor.process_stats.json")
    stats = json.load(open(stat_path, encoding="utf8"))
    max_threads = stats["peak_resources"]["threads"]

    # note that the tile size must be considerably smaller than the design size
    # for klayout to bother threading
    assert (
        max_threads >= step.config["KLAYOUT_XOR_THREADS"]
    ), "XOR threads didn't properly work"
