// MetaMask Integration for Real Web3 DApp
// This file should be included in your HTML when deploying to a web server

class MetaMaskIntegration {
    constructor() {
        this.web3 = null;
        this.userAccount = null;
        this.chainId = null;
        this.isConnected = false;
        this.init();
    }

    async init() {
        // Check if MetaMask is installed
        if (typeof window.ethereum !== 'undefined') {
            console.log('MetaMask is installed!');
            this.setupEventListeners();
            await this.checkConnection();
        } else {
            console.log('MetaMask is not installed');
            this.showMetaMaskInstallPrompt();
        }
    }

    setupEventListeners() {
        // Listen for account changes
        window.ethereum.on('accountsChanged', (accounts) => {
            if (accounts.length === 0) {
                this.handleDisconnect();
            } else {
                this.handleAccountsChanged(accounts);
            }
        });

        // Listen for chain changes
        window.ethereum.on('chainChanged', (chainId) => {
            this.handleChainChanged(chainId);
        });

        // Listen for connection status
        window.ethereum.on('connect', (connectInfo) => {
            this.handleConnect(connectInfo);
        });

        window.ethereum.on('disconnect', (error) => {
            this.handleDisconnect();
        });
    }

    async checkConnection() {
        try {
            const accounts = await window.ethereum.request({ method: 'eth_accounts' });
            if (accounts.length > 0) {
                await this.handleAccountsChanged(accounts);
            }
        } catch (error) {
            console.error('Error checking connection:', error);
        }
    }

    async connectWallet() {
        try {
            // Request account access
            const accounts = await window.ethereum.request({
                method: 'eth_requestAccounts'
            });
            
            await this.handleAccountsChanged(accounts);
            return { success: true, account: accounts[0] };
        } catch (error) {
            console.error('Error connecting wallet:', error);
            return { success: false, error: error.message };
        }
    }

    async handleAccountsChanged(accounts) {
        if (accounts.length === 0) {
            this.handleDisconnect();
        } else {
            this.userAccount = accounts[0];
            this.isConnected = true;
            
            // Get chain ID
            try {
                this.chainId = await window.ethereum.request({ method: 'eth_chainId' });
            } catch (error) {
                console.error('Error getting chain ID:', error);
            }
            
            this.onAccountChanged(this.userAccount, this.chainId);
        }
    }

    async handleChainChanged(chainId) {
        this.chainId = chainId;
        this.onChainChanged(chainId);
        
        // Reload page on chain change (recommended by MetaMask)
        window.location.reload();
    }

    handleConnect(connectInfo) {
        console.log('Connected to MetaMask:', connectInfo);
        this.isConnected = true;
    }

    handleDisconnect() {
        this.userAccount = null;
        this.chainId = null;
        this.isConnected = false;
        this.onDisconnect();
    }

    async getBalance() {
        if (!this.isConnected || !this.userAccount) {
            throw new Error('Wallet not connected');
        }

        try {
            const balance = await window.ethereum.request({
                method: 'eth_getBalance',
                params: [this.userAccount, 'latest']
            });
            
            return this.web3.utils.fromWei(balance, 'ether');
        } catch (error) {
            console.error('Error getting balance:', error);
            throw error;
        }
    }

    async sendTransaction(toAddress, amount, gasLimit = '21000') {
        if (!this.isConnected || !this.userAccount) {
            throw new Error('Wallet not connected');
        }

        try {
            const gasPrice = await window.ethereum.request({
                method: 'eth_gasPrice'
            });

            const transactionParameters = {
                to: toAddress,
                from: this.userAccount,
                value: this.web3.utils.toWei(amount, 'ether'),
                gas: gasLimit,
                gasPrice: gasPrice
            };

            const txHash = await window.ethereum.request({
                method: 'eth_sendTransaction',
                params: [transactionParameters]
            });

            return { success: true, hash: txHash };
        } catch (error) {
            console.error('Error sending transaction:', error);
            return { success: false, error: error.message };
        }
    }

    async switchNetwork(chainId) {
        try {
            await window.ethereum.request({
                method: 'wallet_switchEthereumChain',
                params: [{ chainId: chainId }]
            });
        } catch (error) {
            if (error.code === 4902) {
                // Chain not added to MetaMask
                await this.addNetwork(chainId);
            } else {
                throw error;
            }
        }
    }

    async addNetwork(chainId) {
        const networkParams = this.getNetworkParams(chainId);
        if (networkParams) {
            try {
                await window.ethereum.request({
                    method: 'wallet_addEthereumChain',
                    params: [networkParams]
                });
            } catch (error) {
                console.error('Error adding network:', error);
                throw error;
            }
        }
    }

    getNetworkParams(chainId) {
        const networks = {
            '0x1': { // Ethereum Mainnet
                chainId: '0x1',
                chainName: 'Ethereum Mainnet',
                nativeCurrency: { name: 'Ether', symbol: 'ETH', decimals: 18 },
                rpcUrls: ['https://mainnet.infura.io/v3/YOUR_INFURA_ID'],
                blockExplorerUrls: ['https://etherscan.io']
            },
            '0x5': { // Goerli Testnet
                chainId: '0x5',
                chainName: 'Goerli Testnet',
                nativeCurrency: { name: 'Goerli Ether', symbol: 'ETH', decimals: 18 },
                rpcUrls: ['https://goerli.infura.io/v3/YOUR_INFURA_ID'],
                blockExplorerUrls: ['https://goerli.etherscan.io']
            },
            '0x89': { // Polygon
                chainId: '0x89',
                chainName: 'Polygon',
                nativeCurrency: { name: 'MATIC', symbol: 'MATIC', decimals: 18 },
                rpcUrls: ['https://polygon-rpc.com'],
                blockExplorerUrls: ['https://polygonscan.com']
            }
        };
        
        return networks[chainId];
    }

    // Callback functions - override these in your implementation
    onAccountChanged(account, chainId) {
        console.log('Account changed:', account, 'Chain ID:', chainId);
    }

    onChainChanged(chainId) {
        console.log('Chain changed:', chainId);
    }

    onDisconnect() {
        console.log('Wallet disconnected');
    }

    showMetaMaskInstallPrompt() {
        const prompt = document.createElement('div');
        prompt.innerHTML = `
            <div style="position: fixed; top: 20px; right: 20px; background: #f44336; color: white; padding: 15px; border-radius: 5px; z-index: 1000;">
                <strong>MetaMask Required</strong><br>
                Please install MetaMask to use this DApp.<br>
                <a href="https://metamask.io/download/" target="_blank" style="color: white; text-decoration: underline;">Download MetaMask</a>
            </div>
        `;
        document.body.appendChild(prompt);
        
        // Remove prompt after 10 seconds
        setTimeout(() => {
            if (prompt.parentNode) {
                prompt.parentNode.removeChild(prompt);
            }
        }, 10000);
    }
}

// Usage example:
// const metamask = new MetaMaskIntegration();
// 
// // Override callback functions
// metamask.onAccountChanged = (account, chainId) => {
//     console.log('Connected to account:', account);
//     // Update your UI here
// };
// 
// metamask.onDisconnect = () => {
//     console.log('Wallet disconnected');
//     // Update your UI here
// };
// 
// // Connect wallet
// document.getElementById('connect-btn').addEventListener('click', async () => {
//     const result = await metamask.connectWallet();
//     if (result.success) {
//         console.log('Connected to:', result.account);
//     }
// });
