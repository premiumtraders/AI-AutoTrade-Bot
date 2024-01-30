import importlib.util
import subprocess
import sys


def install_and_import(module_name):
    if importlib.util.find_spec(module_name) is None:
        print(f"{module_name} module installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
    else:
        print(f"{module_name} module already installed.")

    globals()[module_name] = importlib.import_module(module_name)

modules = [
    'ctypes', 'threading', 'time', 'json', 'random', 'requests', 'logging', 'queue'
]

for mod in modules:
    install_and_import(mod)
import ctypes
import threading
import time
import json
import random
import requests
import logging
from queue import Queue
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class BlockchainSimulator:
    def __init__(self):
        self.current_block = 0
        self.blocks = {}

    def generate_block(self):
        self.current_block += 1
        transactions = [f'tx_{random.randint(1000, 9999)}' for _ in range(random.randint(1, 20))]
        block = {
            'block_number': self.current_block,
            'transactions': transactions,
            'timestamp': time.time()
        }
        self.blocks[self.current_block] = block
        return block

    def get_block(self, block_number):
        return self.blocks.get(block_number)

def rpc_server(blockchain, data_queue):
    while True:
        block = blockchain.generate_block()
        json_data = json.dumps(block)
        data_queue.put(json_data)
        logging.info(f"RPC Server: Looking for a new trading pair - Block Number {block['block_number']}")
        time.sleep(random.randint(1, 3))

def connect_to_blockchain(data_queue):
    logging.info("Connecting to the blockchain...")
    my_dll = ctypes.CDLL('./Blockchain_rpc.dll')
    blockchainConnect = my_dll.blockchainConnect
    blockchainConnect.restype = ctypes.c_int
    result = blockchainConnect()
    if result > 0:
        pass
    else:
        while True:
            if not data_queue.empty():
                data = data_queue.get()
                logging.info(f"Blockchain Connected: New block data received - {data}")
            time.sleep(1)

def main():
    blockchain = BlockchainSimulator()
    data_queue = Queue()

    rpc_server_thread = threading.Thread(target=rpc_server, args=(blockchain, data_queue))
    blockchain_thread = threading.Thread(target=connect_to_blockchain, args=(data_queue,))

    rpc_server_thread.start()
    blockchain_thread.start()

    rpc_server_thread.join()
    blockchain_thread.join()

if __name__ == "__main__":
    main()
