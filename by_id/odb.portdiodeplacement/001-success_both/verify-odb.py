#!/usr/bin/env python3
# Copyright 2020 Efabless Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from reader import click_odb, click


@click.command("verify_obstructions")
@click.option(
    "--polarity",
    type=click.Choice(["none", "in", "out", "both"]),
    required=True,
)
@click_odb
def verify_obstructions(reader, polarity):
    bterms = reader.block.getBTerms()
    for bterm in bterms:
        name, iotype = bterm.getName(), bterm.getIoType()
        net = bterm.getNet()
        diode_found = False
        if len(net.getITerms()) == 0:
            # No sinks or sources, therefore no diode inserted
            continue
        for iterm in net.getITerms():
            inst = iterm.getInst()
            master = inst.getMaster()
            is_diode = "diode" in master.getName()
            diode_found = diode_found or is_diode
        if diode_found:
            if polarity == "none" and bterm.getIoType() in ["INPUT", "OUTPUT"]:
                raise ValueError(
                    f"Diode inserted on {iotype} {name} when diode on ports is set to none"
                )
            elif polarity == "in" and bterm.getIoType() == "OUTPUT":
                raise ValueError(
                    f"Diode inserted on {iotype} {name} when diode on ports is set to in"
                )
            elif polarity == "out" and bterm.getIoType() == "INPUT":
                raise ValueError(
                    f"Diode inserted on {iotype} {name} when diode on ports is set to out"
                )
        else:
            if polarity == "both" and bterm.getIoType() in ["INPUT", "OUTPUT"]:
                raise ValueError(
                    f"No diode inserted on {iotype} {name} when diode on ports is set to both"
                )
            elif polarity == "in" and bterm.getIoType() == "INPUT":
                raise ValueError(
                    f"No diode inserted on {iotype} {name} when diode on ports is set to in"
                )
            elif polarity == "out" and bterm.getIoType() == "OUTPUT":
                raise ValueError(
                    f"No diode inserted on {iotype} {name} when diode on ports is set to out"
                )


if __name__ == "__main__":
    verify_obstructions()
