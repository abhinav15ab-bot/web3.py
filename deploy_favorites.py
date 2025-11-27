
from vyper import compile_code
from web3 import Web3
from dotenv import load_dotenv
import os
from encrypt_key import KEYSTORE_PATH
import getpass
from eth_account import Account

load_dotenv()

RPC_URL = os.getenv("RPC_URL")
MY_ADDRESS = os.getenv("MY_ADDRESS")
# PRIVATE_KEY = os.getenv("PRIVATE_KEY")

def main():
    print("Hello from deploy_favorites.py!")
    with open("favorites.vy", "r") as favorites_file:
        favorites_code = favorites_file.read()
        compliation_details = compile_code(favorites_code, output_formats = ["bytecode", "abi"])
        print(compliation_details)
    w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
    favorites_contract = w3.eth.contract(bytecode=compliation_details["bytecode"], abi=compliation_details["abi"])
    # print(favorites_contract)
    # breakpoint()
    print("Building the transaction...")

    nonce = w3.eth.get_transaction_count(MY_ADDRESS)

    transaction = favorites_contract.constructor().build_transaction(
        {

            "nonce": nonce,
            "from": MY_ADDRESS,
            "gasPrice": w3.eth.gas_price,
            
        }
    )
    private_key = decrypt_key()
    signed_transaction = w3.eth.account.sign_transaction(transaction, private_key=private_key)
    print(signed_transaction)
    tx_hash = w3.eth.send_raw_transaction(signed_transaction.raw_transaction)
    print(f"My TX hash is {tx_hash}")
    tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    print(f"Done! Contract deployed at {tx_receipt.contractAddress}")
    # transaction["nonce"] = nonce
    # # transaction["to"] = "0xC6a53a3f4e53aBB9fBA43D1FFF98fB96E5888F23"
    # print(transaction)
    # # breakpoint()

def decrypt_key():
    with open(KEYSTORE_PATH, "r") as fp:
        encrypted_account = fp.read()
        password = getpass.getpass("Enter your password: ")
        key = Account.decrypt(encrypted_account, password)
        print("Decrypted key!")
        return key

if __name__ == "__main__":
    main()

