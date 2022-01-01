import qiskit
from qiskit import IBMQ
print(qiskit.__version__)
IBMQ.save_account('token>')
IBMQ.load_account()