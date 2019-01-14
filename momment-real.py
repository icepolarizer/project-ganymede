from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister, QiskitError
from qiskit import compile, Aer
from qiskit import execute, IBMQ, BasicAer
from qiskit.providers.ibmq import least_busy
from qiskit.tools.monitor import job_monitor

import numpy as np
import math

def xavier(prob):
    try:
        IBMQ.load_accounts()
    except:
        print("""WARNING: There's no connection with the API for remote backends.
                 Have you initialized a file with your personal token?
                 For now, there's only access to local simulator backends...""")

    try:
        print("ARGUMENT: ", prob)
        #if not 0 <= prob <= 1:
        #    print("Prob should be a probability between 0 and 1")
        #    return
        qr = QuantumRegister(1)
        cr = ClassicalRegister(1)
        qc = QuantumCircuit(qr, cr)
        qc.h(qr)
        qc.u3(prob*math.pi, 0, 0, qr[0])
        qc.measure(qr, cr)


        # Compile and run on a real device backend
        # select least busy available device and execute.
        least_busy_device = least_busy(IBMQ.backends(simulator=False))
        print("Running on current least busy device: ", least_busy_device)

        # running the job
        job_exp = execute([qc], backend=least_busy_device, shots=1, max_credits=10)

        job_monitor(job_exp)
        exp_result = job_exp.result()
        counts = exp_result.get_counts(qc)
        print(counts)

        print("Result: ", max(counts.keys(), key=(lambda k: counts[k])))
        if int(min(counts.keys(), key=(lambda k: counts[k]))) == 1:
            return {'signal': prob, 'circuit': qc}
        else:
            return {'signal': 0, 'circuit': qc}

    except QiskitError as ex:
        print('There was an error in the circuit!. Error = {}'.format(ex))

xavier(0.5)
