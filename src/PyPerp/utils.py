import json
import MetaData

def confirmTransferToLayer2(self, receipt, provider):
    meta = MetaData(provider.testnet)
    with open("abi/AmbL2.json") as f:
        layer2AmbAbi = json.load(f)
    layer2AmbAddr = meta.getL2ExtContractAddress("ambBrideOnXDai")
    layer2Amb =  provider.l2.eth.contract(address=layer2AmbAddr,abi=layer2AmbAbi)
    methodId = "0x482515ce"
    for r in receipt:
        log = r["logs"]
        if log.topics[0][:10]==methodId:
            break
    fromMsgId = log.topics[1]
    confirmationFilter = layer2Amb.events.AffirmationCompleted.createFilter(fromBlock="latest",argument_filters={'toMsgId':fromMsgId})  
    while True:
        for c in confirmationFilter:
            print("Transfer completed")
            return 

def confirmTransferToLayer1(self, reciept, provider):
    meta = MetaData(provider.testnet)
    with open("abi/AmbL1.json") as f:
        layer1AmbAbi = json.load(f)
    lauer1AmbAddr = meta.getL1ExtContractAddress("ambBridgeOnEth")
    layer1Amb = provider.l1.eth.contract(address=layer1AmbAddr,abi=layer1AmbAbi)
    methodId = "0x520d2afd"
    for r in receipt:
        log = r["logs"]
        if log.topics[0][:10]==methodId:
            break
    fromMsgId = log.topics[1]
    confirmationFilter = layer1Amb.events.RelayedMessage.createFilter(fromBlock="latest",argument_filters={'toMsgId':fromMsgId})  
    while True:
        for c in confirmationFilter:
            print("Transfer completed")
            return 