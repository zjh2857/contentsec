import requests
import json
import pickle
from util import ac_auto


while True :
    tradehash = input()
    session = requests.Session()
    method = 'debug_traceTransaction'
    params = [tradehash,{}]
    payload= {"jsonrpc":"2.0",
            "method":method,
            "params":params,
            "id":1}
    headers = {'Content-type': 'application/json'}
    response = session.post('http://172.23.144.1:8545', json=payload, headers=headers)
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
    method = 'eth_getTransactionReceipt'
    params = [tradehash]
    payload= {"jsonrpc":"2.0",
            "method":method,
            "params":params,
            "id":1}
    headers = {'Content-type': 'application/json'}
    response = session.post('http://172.23.144.1:8545', json=payload, headers=headers)
    to = response.json()["result"]["to"]
    try:
        f = open(to,"rb")
        ac = pickle.load(f)
        f.close()
    except:
        print("aaa")
        ac = ac_auto()
    ac.search(execlist)
    
