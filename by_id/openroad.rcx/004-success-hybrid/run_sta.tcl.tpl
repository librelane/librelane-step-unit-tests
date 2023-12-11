read_liberty {lib}
read_verilog {nl}
read_verilog ./spm.nl.v
link_design manual_macro_placement_test
read_spef {spef_file}
read_spef -path spm_inst_0 ./spm.{corner}.spef
read_spef -path spm_inst_1 ./spm.{corner}.spef
report_parasitic_annotation -report_unannotated > out.log