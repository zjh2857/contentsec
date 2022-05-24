import requests
import json
from util import ac
session = requests.Session()
method = 'debug_traceTransaction'
params = ["0xf5ac1d8d799659ed08fba44e73ef9ee5451898e43f6d43a78a58bc9626b5277d"]
payload= {"jsonrpc":"2.0",
           "method":method,
           "params":params,
           "id":1}
headers = {'Content-type': 'application/json'}
response = session.post('http://localhost:8545', json=payload, headers=headers)

insts = response.json()["result"]["structLogs"]
label = set()
for inst in insts:
    pc = inst['pc']
    op = inst['op']
    stack = inst['stack']
    if(op == "JUMP" or op == "JUMPI"):
        label.add(pc+1)
        label.add(int(stack[-1],16))
execlist = []
for inst in insts:
    pc = inst['pc']
    if(pc in label):
        execlist.append(pc)

ac = ac()
ac.add(execlist)
ac.fail()
ac.search(execlist)