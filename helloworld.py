from qiskit import *

qr = qiskit.QuantumRegister(2) # 2 qubits register
cr = qiskit.ClassicalRegister(2) # 2 classical bits register
circuit = qiskit.QuantumCircuit(qr, cr) # quantum circuit
# %matplotlib inline
# qc.draw()
# this only works in jupyter notebook
circuit.h(qr[0]) # Hadamard gate
circuit.cx(qr[0], qr[1]) # CNOT
print(circuit)