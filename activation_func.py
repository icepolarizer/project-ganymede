from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from qiskit import compile, Aer
import math

def xavier(prob):
    if not 0 <= prob <= 1:
        print("Prob should be a probability between 0 and 1")
        return
    qr = QuantumRegister(1)
    cr = ClassicalRegister(1)
    qc = QuantumCircuit(qr, cr)
    qc.h(qr)
    qc.u3(prob*math.pi, 0, 0, qr[0])
    qc.measure(qr, cr)

    qc.draw()

    backend = Aer.get_backend('qasm_simulator')
    qobj = compile(qc, backend, shots=1)
    job = backend.run(qobj)
    result = job.result()
    counts = result.get_counts()
    # print(counts)
    return max(counts)

print(xavier(0.01))