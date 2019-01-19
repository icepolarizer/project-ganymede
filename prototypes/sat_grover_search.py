from qiskit import Aer
from qiskit_aqua.components.oracles import SAT
from qiskit_aqua.algorithms import Grover

sat_cnf = """
c Example DIMACS 3-sat
p cnf 3 5
-1 -2 -3 0
1 -2 3 0
1 2 -3 0
1 -2 -3 0
-1 2 3 0
"""

backend = Aer.get_backend('qasm_simulator')
oracle = SAT(sat_cnf)
algorithm = Grover(oracle)
result = algorithm.run(backend)

print(result["result"])