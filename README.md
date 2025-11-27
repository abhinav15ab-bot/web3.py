# Web3 Favorites cu

🚀 Project Overview

This project shows how to deploy Vyper smart contracts using raw Python, while keeping private keys secure and making the entire setup reproducible for any developer using uv.

📌 What This Project Does
1. Deploy Vyper Contracts from Python

Compile Vyper contracts using Python

Deploy them using web3.py

Interact with the blockchain without relying on heavy frameworks

2. Secure Private Key Encryption

Convert your private key into an encrypted JSON keystore

Protect it with a password

Decrypt it only when needed

Use it to safely sign transactions

3. Reproducible Environment with uv

Consistent dependency management

Fast setup for any engineer

Ensures the project runs the same everywhere

🎓 What You Will Learn
1. What an Ethereum Transaction Contains

You will understand each part of a transaction:

nonce

to

value

gas

maxFeePerGas / maxPriorityFeePerGas

data

chainId

signature

2. What a JSON Keystore Is

A JSON keystore is:

An encrypted version of your private key

Password-protected

The same format used by MetaMask and Ethereum clients

3. How to Store Private Keys Safely

You will learn:

Using encrypted keystore files

Never putting raw private keys in code

Keeping secrets out of GitHub

Signing transactions locally

