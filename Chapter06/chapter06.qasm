OPENQASM 2.0;
include "qelib1.inc";

qreg q[5];
creg c[5];

cx q[2],q[1];
s q[3];
y q[4];
x q[1];
h q[2];
z q[3];
y q[4];
x q[1];
t q[2];
z q[3];
tdg q[2];
h q[2];
cx q[2],q[1];
sdg q[3];
measure q[0] -> c[0];
measure q[1] -> c[1];
measure q[2] -> c[2];
measure q[3] -> c[3];
measure q[4] -> c[4];
