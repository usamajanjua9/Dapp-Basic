# Simple DApp - Minimal Blockchain Viewer

A minimal decentralized application built with Streamlit for viewing wallet information.

## Features

- 🔗 **Wallet Connection**: Connect wallet with manual address input
- 💰 **Balance Display**: View real wallet balance from blockchain
- 📱 **Simple UI**: Clean, minimal interface built with Streamlit

## Installation

1. **Clone or download this repository**
2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Running the App

1. **Navigate to the project directory:**
   ```bash
   cd streamlit-dapp
   ```

2. **Run the Streamlit app:**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser** and go to the URL shown in the terminal (usually `http://localhost:8501`)

## Usage

1. **Connect Wallet**: Enter a valid Ethereum address in the sidebar
2. **View Info**: See wallet address, balance, and network information
3. **Refresh**: Update balance and wallet information

## Project Structure

```
streamlit-dapp/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Dependencies

- **Streamlit**: Web app framework
- **Web3.py**: Ethereum interaction library

## Notes

- This is a **minimal application** for viewing wallet information
- Uses public RPC endpoints for blockchain data
- Wallet connection is manual (enter address) for simplicity

