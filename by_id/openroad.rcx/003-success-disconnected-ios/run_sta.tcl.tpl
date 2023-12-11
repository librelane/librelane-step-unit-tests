read_liberty {lib}
read_verilog {nl}
read_verilog ./aes_example.v
link_design user_project_wrapper
read_spef {spef_file}
read_spef -path mprj ./aes_example.{corner}.spef
report_parasitic_annotation -report_unannotated > out.log