import streamlit as st
from web3 import Web3

# Page configuration
st.set_page_config(
    page_title="Simple DApp",
    page_icon="🔗",
    layout="wide"
)

# Initialize session state
if 'wallet_connected' not in st.session_state:
    st.session_state.wallet_connected = False
if 'wallet_address' not in st.session_state:
    st.session_state.wallet_address = None
if 'web3' not in st.session_state:
    st.session_state.web3 = None

# Simple network configuration
NETWORKS = {
    1: "Ethereum Mainnet",
    5: "Goerli Testnet",
    137: "Polygon",
    80001: "Mumbai Testnet"
}

def get_web3_provider():
    """Get Web3 provider"""
    return Web3(Web3.HTTPProvider("https://eth.llamarpc.com"))

def connect_wallet():
    """Connect wallet with manual address input"""
    wallet_address = st.text_input("Enter wallet address:", 
                                 placeholder="0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6")
    
    if st.button("Connect"):
        if wallet_address and Web3.is_address(wallet_address):
            st.session_state.wallet_connected = True
            st.session_state.wallet_address = Web3.to_checksum_address(wallet_address)
            st.session_state.web3 = get_web3_provider()
            st.success("Wallet connected!")
            st.rerun()
        else:
            st.error("Invalid address!")

def disconnect_wallet():
    """Disconnect wallet"""
    st.session_state.wallet_connected = False
    st.session_state.wallet_address = None
    st.session_state.web3 = None
    st.success("Disconnected!")
    st.rerun()

def get_balance():
    """Get wallet balance"""
    if st.session_state.wallet_connected and st.session_state.web3:
        try:
            balance_wei = st.session_state.web3.eth.get_balance(st.session_state.wallet_address)
            balance_eth = st.session_state.web3.from_wei(balance_wei, 'ether')
            return f"{balance_eth:.6f} ETH"
        except:
            return "Error"
    return "0 ETH"

# Sidebar
with st.sidebar:
    st.title("🔗 Simple DApp")
    
    if not st.session_state.wallet_connected:
        connect_wallet()
    else:
        st.success("✅ Connected")
        st.info(f"Address: {st.session_state.wallet_address[:10]}...")
        st.info(f"Balance: {get_balance()}")
        
        if st.button("Disconnect"):
            disconnect_wallet()

# Main content
st.title("🏠 Simple DApp")
st.markdown("A minimal blockchain application for viewing wallet information.")

if st.session_state.wallet_connected:
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Wallet Info")
        st.info(f"**Address:** {st.session_state.wallet_address}")
        st.info(f"**Balance:** {get_balance()}")
        st.info(f"**Network:** Ethereum Mainnet")
    
    with col2:
        st.subheader("Quick Actions")
        if st.button("Refresh Balance"):
            st.rerun()
        
        if st.button("Copy Address"):
            st.success("Address copied!")
else:
    st.info("Connect your wallet using the sidebar to get started!")

# Footer
st.divider()
st.markdown("**Simple DApp** - Minimal blockchain viewer")
