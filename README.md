# Web3 Favorites cu

what does this project do?
1. Deploy our vyper contract from raw python
This project teaches you how to:

  Write a Vyper smart contract
  Compile it using Python
  Deploy it to a blockchain (like Sepolia or Anvil) using web3.py
  No frameworks like Brownie or Foundry — pure Python!

So you learn how blockchain actually works “under the hood.”

2. Encrypt our private keys locally, and use then to sign transactions

Normally people store private keys in .env, which is unsafe.
In this project, you learn to:

  Encrypt your private key into a JSON keystore file (same format MetaMask uses)
  Protect it with a password
  Decrypt it inside Python
  Use it to sign transactions securely

So no one can steal your private key.

3. This is going to be reproducible by other engineers using uv with python
This means:

  The project can be set up by any engineer
  The environment, dependencies, and versions are automatically installed
  Reproducible = works the same on any machine

This is how professional teams manage Python blockchain code.


what are going to learn?
1. What is a transaction comprised of?

You will learn each part of a blockchain transaction:
nonce – how many transactions your account has sent
to – receiver address
value – ETH you send
gas – max gas to use
gasPrice / maxFeePerGas – how much you pay
data – encoded smart-contract function call
chainId – protects against replay attacks
signature – created using your private key
After signing, this becomes a raw transaction that nodes can accept.

2. what is json keystore?

A JSON keystore is a password-protected private key file.
It is a .json file
Encrypted using strong encryption (AES-128-CTR + PBKDF2 or scrypt)
Used by MetaMask, Geth, OpenEthereum, etc.
You unlock it by giving your password, then your program can use the private key to sign transactions.
It is MUCH safer than keeping your private key in plain text.

3. How can I safely store my private keys?

You will learn the safe ways:

✅ Recommended

Use encrypted JSON keystore

Store password in a secure system (not in code)

Never expose raw private key on GitHub

Use .gitignore

Use environment variables only for non-secret keys

❌ Never do

Never put private key in code

Never upload to GitHub

Never send to anyone

Never store unencrypted keys in public folders

This project teaches you the professional method used by real blockchain engineers.




