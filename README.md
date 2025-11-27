🚀 Vyper Contract Deployment & Secure Key Management

A hands-on project built with Python, Vyper, and web3.py, designed to teach how to deploy smart contracts, sign transactions, and securely manage private keys.
    This project also uses uv to provide a fully reproducible environment for any developer.

✨ Features

   -📝 Deploy Vyper Contracts using pure Python

  -🔐 Encrypted JSON Keystore for private key protection

  -✍️ Local Transaction Signing with decrypted keys

  -⚙️ Reproducible Environment powered by uv

  -🧩 Under-the-Hood Learning of how web3.py works

⚙️ Tech Stack

      Vyper – Smart contract language
    
      Python & web3.py – Deployment + blockchain interactions
    
      JSON Keystore – Secure private key format
    
      uv – Modern dependency & environment manager

📚 What You Will Learn

  -🧱 What makes up an Ethereum transaction (nonce, gas, chainId, data, etc.)

  -🔒 What a JSON keystore is and why it’s used

  -🗝️ How to safely store, encrypt, and decrypt private keys

📤 How to deploy and interact with Vyper contracts using raw Python

├── contracts/
│   └── favorites.vy
│


├── scripts/
│   ├── compile_contract.py
│   ├── encrypt_key.py
│   ├── decrypt_key.py
│   └── deploy_contract.py
│


├── .env
├── uv.lock
└── pyproject.toml

## 🙌 About the Author  

👤 **Abhinav Malik**  


🔗 **Connect with me:**  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Abhinav%20Malik-blue?logo=linkedin&logoColor=white)](https://www.linkedin.com/in/abhinav-malik-16b493277/)  
[![GitHub](https://img.shields.io/badge/GitHub-abhinav15ab--bot-black?logo=github)](https://github.com/abhinav15ab-bot)

---


🚀 Getting Started
    1️⃣ Install uv
    
    pip install uv

    2️⃣ Clone the Repository

    git clone https://github.com/<your-username>/<your-repo>.git
    cd <your-repo>

    3️⃣ Install Dependencies

    uv sync

    4️⃣ Compile Contract

    python scripts/compile_contract.py

    5️⃣ Encrypt Your Private Key

    python scripts/encrypt_key.py

    6️⃣ Deploy the Contract

    python scripts/deploy_contract.py

    📊 Example Output

    nonce: 1
    gas: 21000
    chainId: 11155111
    signature: 0xabc...
    contract deployed at: 0x1234...



