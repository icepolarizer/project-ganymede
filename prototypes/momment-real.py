from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QiskitError
from qiskit import compile, Aer
from qiskit import execute, IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor

import numpy as np
import math


try:
    IBMQ.load_accounts()
except:
    print("""WARNING: There's no connection with the API for remote backends.
             Have you initialized a file with your personal token?
             For now, there's only access to local simulator backends...""")

try:
    #if not 0 <= prob <= 1:
    #    print("Prob should be a probability between 0 and 1")
    #    return
    qr = QuantumRegister(4)
    cr = ClassicalRegister(4)
    qc = QuantumCircuit(qr, cr)
    qc.h(qr)
    qc.measure(qr, cr)


    # Compile and run on a real device backend
    # select least busy available device and execute.
    least_busy_device = least_busy(IBMQ.backends(simulator=False))
    print("[+] Generating Random Qbit value (0-255 in Decimal)")
    print("[+] Running on current least busy device: ", least_busy_device)

    # running the job
    job_exp = execute([qc], backend=least_busy_device, shots=1, max_credits=10)

    job_monitor(job_exp)
    exp_result = job_exp.result()
    counts = exp_result.get_counts(qc)

    print("[+] Random int has successfully generated.")
    print(counts)

    rand_bin = max(counts.keys(), key=(lambda k: counts[k]))
    print("Result: ", rand_bin)

    print("In Decimal: ", int(rand_bin, 2))

except QiskitError as ex:
    print('There was an error in the circuit!. Error = {}'.format(ex))

