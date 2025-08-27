import streamlit as st
import json
from web3 import Web3
from streamlit_option_menu import option_menu

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

def connect_wallet():
    """Connect to MetaMask or other Web3 wallet"""
    try:
        # This is a simplified version - in a real app you'd use proper Web3 connection
        # For demo purposes, we'll simulate wallet connection
        st.session_state.wallet_connected = True
        st.session_state.wallet_address = "0x742d35Cc6634C0532925a3b8D4C9db96C4b4d8b6"
        st.session_state.web3 = Web3()
        st.success("Wallet connected successfully! 🎉")
        st.rerun()
    except Exception as e:
        st.error(f"Failed to connect wallet: {str(e)}")

def disconnect_wallet():
    """Disconnect wallet"""
    st.session_state.wallet_connected = False
    st.session_state.wallet_address = None
    st.session_state.web3 = None
    st.success("Wallet disconnected successfully! 👋")
    st.rerun()

def get_balance():
    """Get wallet balance (simulated)"""
    if st.session_state.wallet_connected:
        # Simulated balance for demo
        return "0.5 ETH"
    return "0 ETH"

# Sidebar navigation
with st.sidebar:
    st.title("🔗 Simple DApp")
    
    # Wallet connection section
    st.header("Wallet")
    if not st.session_state.wallet_connected:
        if st.button("Connect Wallet", type="primary", use_container_width=True):
            connect_wallet()
    else:
        st.success("✅ Connected")
        st.info(f"Address: {st.session_state.wallet_address[:10]}...")
        st.info(f"Balance: {get_balance()}")
        if st.button("Disconnect", type="secondary", use_container_width=True):
            disconnect_wallet()
    
    st.divider()
    
    # Navigation menu
    selected = option_menu(
        menu_title="Navigation",
        options=["Home", "Wallet Info", "Transactions", "Settings"],
        icons=["house", "wallet2", "arrow-left-right", "gear"],
        menu_icon="cast",
        default_index=0,
    )

# Main content area
if selected == "Home":
    st.title("🏠 Welcome to Simple DApp")
    st.markdown("""
    This is a basic decentralized application built with Streamlit.
    
    **Features:**
    - 🔗 Wallet connection/disconnection
    - 💰 Balance display
    - 📱 Responsive design
    - 🎨 Clean UI
    
    **Getting Started:**
    1. Connect your wallet using the sidebar
    2. Explore the different sections
    3. View your wallet information
    """)
    
    # Quick actions
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Status", "Active" if st.session_state.wallet_connected else "Inactive")
    
    with col2:
        st.metric("Network", "Ethereum Mainnet")
    
    with col3:
        st.metric("Gas Price", "25 Gwei")

elif selected == "Wallet Info":
    st.title("💳 Wallet Information")
    
    if st.session_state.wallet_connected:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Connection Details")
            st.info(f"**Status:** Connected")
            st.info(f"**Address:** {st.session_state.wallet_address}")
            st.info(f"**Balance:** {get_balance()}")
            st.info(f"**Network:** Ethereum Mainnet")
        
        with col2:
            st.subheader("Quick Actions")
            if st.button("Refresh Balance", use_container_width=True):
                st.info("Balance refreshed!")
            
            if st.button("Copy Address", use_container_width=True):
                st.success("Address copied to clipboard!")
            
            if st.button("Export Private Key", use_container_width=True):
                st.warning("⚠️ Never share your private key!")
    else:
        st.warning("Please connect your wallet first!")
        if st.button("Connect Wallet", type="primary"):
            connect_wallet()

elif selected == "Transactions":
    st.title("📊 Transaction History")
    
    if st.session_state.wallet_connected:
        # Simulated transaction data
        transactions = [
            {"hash": "0x1234...5678", "type": "Send", "amount": "0.1 ETH", "status": "Confirmed", "time": "2 hours ago"},
            {"hash": "0x8765...4321", "type": "Receive", "amount": "0.05 ETH", "status": "Confirmed", "time": "1 day ago"},
            {"hash": "0x9999...8888", "type": "Swap", "amount": "100 USDC", "status": "Pending", "time": "3 hours ago"}
        ]
        
        for tx in transactions:
            with st.container():
                col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
                col1.write(f"**{tx['hash']}**")
                col2.write(tx['type'])
                col3.write(tx['amount'])
                col4.write(tx['status'])
                st.divider()
    else:
        st.warning("Please connect your wallet to view transactions!")

elif selected == "Settings":
    st.title("⚙️ Settings")
    
    st.subheader("App Preferences")
    theme = st.selectbox("Theme", ["Light", "Dark", "Auto"])
    language = st.selectbox("Language", ["English", "Spanish", "French"])
    
    st.subheader("Wallet Settings")
    auto_connect = st.checkbox("Auto-connect wallet on startup")
    show_balance = st.checkbox("Show balance in sidebar")
    
    st.subheader("Notifications")
    email_notifications = st.checkbox("Email notifications")
    push_notifications = st.checkbox("Push notifications")
    
    if st.button("Save Settings", type="primary"):
        st.success("Settings saved successfully!")

# Footer
st.divider()
st.markdown("---")
st.markdown("**Simple DApp** - Built with ❤️ using Streamlit and Web3")
st.markdown("*This is a demo application for educational purposes*")
