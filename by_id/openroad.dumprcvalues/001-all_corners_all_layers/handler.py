from pathlib import Path
from pprint import pprint
from decimal import Decimal

from parser import parse_report_file

from librelane.common import Filter


def compute_average_rc(
    corners_data, clock_layers, signal_layers, direction_by_layer_name
):
    results = {}

    for corner_name, layer_data in corners_data.items():
        results[corner_name] = {
            "clock": {
                "HORIZONTAL": {"cap": Decimal(0), "res": Decimal(0), "count": 0},
                "VERTICAL": {"cap": Decimal(0), "res": Decimal(0), "count": 0},
            },
            "signal": {
                "HORIZONTAL": {"cap": Decimal(0), "res": Decimal(0), "count": 0},
                "VERTICAL": {"cap": Decimal(0), "res": Decimal(0), "count": 0},
            },
        }

        for layer_name, rc_data in layer_data.items():
            layer_types = []
            if layer_name in clock_layers:
                layer_types.append("clock")
            if layer_name in signal_layers:
                layer_types.append("signal")

            for layer_type in layer_types:
                direction = direction_by_layer_name.get(layer_name)
                if direction:
                    direction_key = direction.upper()  # Convert to uppercase
                    results[corner_name][layer_type][direction_key]["cap"] += rc_data[
                        "cap"
                    ]
                    results[corner_name][layer_type][direction_key]["res"] += rc_data[
                        "res"
                    ]
                    results[corner_name][layer_type][direction_key]["count"] += 1

        # Calculate averages
        for layer_type in ["clock", "signal"]:
            for direction in ["HORIZONTAL", "VERTICAL"]:  # Use all caps here
                count = results[corner_name][layer_type][direction]["count"]
                if count > 0:
                    results[corner_name][layer_type][direction]["cap"] /= count
                    results[corner_name][layer_type][direction]["res"] /= count
                else:
                    results[corner_name][layer_type][direction]["cap"] = Decimal(0)
                    results[corner_name][layer_type][direction]["res"] = Decimal(0)

    return results


def post_process_averages(averaged_rc_data):
    post_processed_results = {}

    for corner, layer_data in averaged_rc_data.items():
        post_processed_results[corner] = {}

        for layer_type in ["signal", "clock"]:
            post_processed_results[corner][layer_type] = {}

            horizontal_data = layer_data[layer_type]["HORIZONTAL"]
            vertical_data = layer_data[layer_type]["VERTICAL"]

            if layer_type == "signal":
                avg_cap = (horizontal_data["cap"] + vertical_data["cap"]) / 2
                avg_res = (horizontal_data["res"] + vertical_data["res"]) / 2
                post_processed_results[corner][layer_type]["cap"] = avg_cap
                post_processed_results[corner][layer_type]["res"] = avg_res

            elif layer_type == "clock":
                if horizontal_data["res"] != 0:
                    post_processed_results[corner][layer_type]["res"] = horizontal_data[
                        "res"
                    ]
                else:
                    avg_res = (horizontal_data["res"] + vertical_data["res"]) / 2
                    post_processed_results[corner][layer_type]["res"] = avg_res

                avg_cap = (horizontal_data["cap"] + vertical_data["cap"]) / 2
                post_processed_results[corner][layer_type]["cap"] = avg_cap

    return post_processed_results


def deep_diff(dict1, dict2, path="", *, i_hate_ieee_754_threshold=Decimal("0")):
    diff = {}

    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())

    added_keys = keys2 - keys1
    removed_keys = keys1 - keys2
    common_keys = keys1 & keys2

    for key in added_keys:
        diff[path + "." + key if path else key] = [None, dict2[key]]

    for key in removed_keys:
        diff[path + "." + key if path else key] = [dict1[key], None]

    for key in common_keys:
        new_path = path + "." + key if path else key
        val1 = dict1[key]
        val2 = dict2[key]

        if isinstance(val1, dict) and isinstance(val2, dict):
            nested_diff = deep_diff(
                val1,
                val2,
                new_path,
                i_hate_ieee_754_threshold=i_hate_ieee_754_threshold,
            )
            diff.update(nested_diff)
        elif val1 == val2:
            pass
        elif isinstance(val1, Decimal) or isinstance(val2, Decimal):
            abs_diff = abs(val1 - val2)
            diff_ratio = abs_diff / val1
            if diff_ratio > i_hate_ieee_754_threshold:
                diff[new_path] = [val1, val2]
        else:
            diff[new_path] = [val1, val2]

    return diff


def handle(step):
    step_dir = Path(step.step_dir)

    tlef_values = parse_report_file(step_dir / "tlef_values.rpt")
    # layer_values_after = parse_report_file(step_dir / "layer_values_after.rpt")
    resizer_values_after = parse_report_file(step_dir / "resizer_values_after.rpt")

    pnr_corners = step.config["PNR_CORNERS"]

    all_corners = set(pnr_corners)

    all_rt_layers = set(tlef_values["routing_layers"].keys())
    all_vias = set(tlef_values["vias"].keys())
    used_rt_layers = set()

    direction_by_layer_name = {}
    adding = 0
    for name, info in tlef_values["routing_layers"].items():
        direction_by_layer_name[name] = info["direction"]
        if name == step.config["RT_MIN_LAYER"]:
            adding = 1
        if adding:
            used_rt_layers.add(name)
        if name == step.config["RT_MAX_LAYER"]:
            adding = 0

    # -- Layers --
    used_layer_corners = set()
    layer_rc_values_in = {}

    for corner_wildcard, metal_layers in step.config["LAYERS_RC"].items():
        for corner in Filter([corner_wildcard]).filter(pnr_corners):
            layer_rc_values_in.setdefault(corner, {})
            layer_rc_values_in[corner].update(**metal_layers)
            for missing_layer in all_rt_layers - set(metal_layers.keys()):
                layer_rc_values_in[corner][missing_layer] = {
                    "res": Decimal("0"),
                    "cap": Decimal("0"),
                }
            used_layer_corners.add(corner)

    for corner in all_corners - used_layer_corners:
        layer_rc_values_in.setdefault(corner, {})
        for name, entry in tlef_values["routing_layers"].items():
            layer_rc_values_in[corner][name] = {
                "cap": entry["cap"],
                "res": entry["res"],
            }
    if len(used_layer_corners) == 0:
        # No point comparing the output, it's all zeroes
        pass
    else:
        layer_rc_values_out = {}
        for corner, info in resizer_values_after.items():
            layer_rc_values_out[corner] = {}
            for entry in info["rt_layer_rc_values"]:
                layer_rc_values_out[corner][entry["name"]] = {
                    "cap": entry["cap"],
                    "res": entry["res"],
                }

        diff = deep_diff(layer_rc_values_in, layer_rc_values_out)
        print("Diff input/output layer rc values:")
        pprint(diff)
        print("---")
        assert (
            len(diff) == 0
        ), "differences found between input and output layer rc values"

    signal_layers = set(step.config["SIGNAL_WIRE_RC_LAYERS"] or used_rt_layers)
    clock_layers = set(step.config["CLOCK_WIRE_RC_LAYERS"] or used_rt_layers)
    expected_averages_raw = compute_average_rc(
        layer_rc_values_in, clock_layers, signal_layers, direction_by_layer_name
    )
    expected_averages = post_process_averages(expected_averages_raw)

    wire_rc_averages_out = {}
    for corner, info in resizer_values_after.items():
        wire_rc_averages_out.setdefault(corner, {})
        for entry in info["estimation_rc_values"]:
            wire_rc_averages_out[corner][entry["name"].lower()] = {
                "res": entry["res"],
                "cap": entry["cap"],
            }

    diff = deep_diff(
        expected_averages,
        wire_rc_averages_out,
        i_hate_ieee_754_threshold=Decimal("0.0001"),
    )
    print("Diff expected/actual wire rc values:")
    pprint(diff)
    print("---")
    assert len(diff) == 0, "differences found in the wire rc values used for estimation"

    # -- Vias --
    used_via_corners = set()
    via_r_values_in = {}

    for corner_wildcard, vias in step.config["VIAS_R"].items():
        for corner in Filter([corner_wildcard]).filter(pnr_corners):
            via_r_values_in.setdefault(corner, {})
            via_r_values_in[corner].update(**vias)
            for missing_via in all_vias - set(vias.keys()):
                via_r_values_in[corner][missing_via] = {
                    "res": Decimal("0"),
                }
            used_via_corners.add(corner)

    if len(used_via_corners) == 0:
        # Nothing to verify.
        pass
    else:
        for corner in all_corners - used_via_corners:
            via_r_values_in.setdefault(corner, {})
            for name, entry in tlef_values["vias"].items():
                via_r_values_in[corner][entry["name"]] = {
                    "res": entry["res"],
                }

            for entry in info["via_r_values"]:
                via_r_values_in[corner][entry["name"]] = {
                    "res": entry["res"],
                }

        via_r_values_out = {}
        for corner, info in resizer_values_after.items():
            via_r_values_out[corner] = {}
            for entry in info["via_r_values"]:
                via_r_values_out[corner][entry["name"]] = {
                    "res": entry["res"],
                }

        diff = deep_diff(via_r_values_in, via_r_values_out)
        print("Diff input/output via R values:")
        pprint(diff)
        print("---")
        assert len(diff) == 0, "differences found between input and output via r values"
