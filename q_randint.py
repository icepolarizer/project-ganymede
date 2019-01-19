from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QiskitError
from qiskit import compile, Aer
from qiskit import execute, IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor

import numpy as np
import math


qr = QuantumRegister(8)
cr = ClassicalRegister(8)
qc = QuantumCircuit(qr, cr)
qc.h(qr)
qc.measure(qr, cr)

qc.draw()

backend = Aer.get_backend('qasm_simulator')
qobj = compile(qc, backend, shots=1)
job = backend.run(qobj)
result = job.result()
counts = result.get_counts()
print(counts)

rand_bin = max(counts.keys(), key=(lambda k: counts[k]))
print("Result: ", rand_bin)

print("In Decimal: ", int(rand_bin, 2))
