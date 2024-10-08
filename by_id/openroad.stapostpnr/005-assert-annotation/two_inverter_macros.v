module two_inverter_macros (VGND,
    VPWR,
    in,
    out);
 input VGND;
 input VPWR;
 input in;
 output out;

 wire glue;

 inverter inv_1 (.VGND(VGND),
    .VPWR(VPWR),
    .in(in),
    .out(glue));
 inverter inv_2 (.VGND(VGND),
    .VPWR(VPWR),
    .in(glue),
    .out(out));
endmodule
