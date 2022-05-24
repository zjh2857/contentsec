import requests
import json

from sqlalchemy import true
from util import ac


while true :
    tradehash = input()
    session = requests.Session()
    method = 'debug_traceTransaction'
    params = [tradehash]
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
    session = requests.Session()
    method = 'eth_getTransaction'
    params = [tradehash]
    payload= {"jsonrpc":"2.0",
            "method":method,
            "params":params,
            "id":1}
    headers = {'Content-type': 'application/json'}
    response = session.post('http://localhost:8545', json=payload, headers=headers)
    to = response.json()
    print(to)
    ac = ac()
    ac.add(execlist)
    ac.fail()
    ac.search(execlist)