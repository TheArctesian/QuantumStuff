import qiskit
from qiskit import IBMQ

# test if qiskit is installed
print(qiskit.__version__)

# access pass phrase from pass.txt
token = open("pass.txt", "r")
# load the IBMQ account
IBMQ.save_account(token.read())

#account info
print(IBMQ.load_account())