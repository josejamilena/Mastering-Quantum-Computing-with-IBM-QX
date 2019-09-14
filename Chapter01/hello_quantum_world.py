from qiskit import(
  QuantumRegister,
  ClassicalRegister,
  QuantumCircuit,
  execute,
  Aer)
from qiskit.visualization import plot_histogram
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
#matplotlib.use('WebAgg')
import time

backend = Aer.get_backend('qasm_simulator')
q = QuantumRegister(5)
c = ClassicalRegister(5)
qc = QuantumCircuit(q, c)
qc.measure(q, c)
job_exp = execute(qc, backend=backend)

fig = plot_histogram(job_exp.result().get_counts(qc), title="hello_quantum_world.png")
fig.savefig("hello_quantum_world.png")
plt.show()
