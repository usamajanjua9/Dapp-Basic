# Simple DApp - Streamlit Web3 Application

A basic decentralized application built with Streamlit that demonstrates wallet connection/disconnection functionality.

## Features

- 🔗 **Wallet Connection**: Connect and disconnect Web3 wallets
- 💰 **Balance Display**: View wallet balance and information
- 📱 **Responsive Design**: Clean, modern UI built with Streamlit
- 🧭 **Navigation**: Multiple sections including Home, Wallet Info, Transactions, and Settings
- 🎨 **Modern UI**: Beautiful interface with icons and proper styling

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

1. **Connect Wallet**: Click the "Connect Wallet" button in the sidebar
2. **Explore Sections**: Navigate between different sections using the sidebar menu
3. **View Wallet Info**: Check your connected wallet details and balance
4. **Browse Transactions**: View simulated transaction history
5. **Customize Settings**: Adjust app preferences and wallet settings

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
- **streamlit-option-menu**: Enhanced navigation menu

## Notes

- This is a **demo application** for educational purposes
- Wallet connection is **simulated** - in a real app you'd integrate with MetaMask or other Web3 providers
- Transaction data is **simulated** for demonstration
- The app uses Streamlit's session state to maintain wallet connection status

## Customization

You can easily customize this app by:
- Adding real Web3 wallet integration
- Implementing actual blockchain transactions
- Adding more features like token swaps, NFT display, etc.
- Customizing the UI theme and colors
- Adding database integration for persistent data

## Support

This is a basic template that you can build upon. Feel free to modify and extend it for your specific use case!
