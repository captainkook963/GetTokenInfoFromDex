#https://eth-mainnet.g.alchemy.com/v2/5_o6kAwJGucjUehzCwCSdxODhW88jFAF

from web3 import Web3
from abi import ERC20ABI, LPABI
import decimal  
#import IUniswapV2Pair from '@uniswap/v2-core/contracts/interfaces/IUniswapV2Pair.json';


node = 'https://eth-mainnet.g.alchemy.com/v2/5_o6kAwJGucjUehzCwCSdxODhW88jFAF'
web3 = Web3(Web3.HTTPProvider(node))

#pause here to make sure you're connected
#print(web3.is_connected())

#Pair Address
lpAddress = web3.to_checksum_address('0x41F50f520f5095fC8403DF083285232B822611c3')
lpContract = web3.eth.contract(address=lpAddress, abi=LPABI)

def token_price():
    token0, token1 = lpContract.functions.token0().call(), lpContract.functions.token1().call()
    reserves = lpContract.functions.getReserves().call()
    print(reserves, "pooled SOL, Pooled WETH, IDK")
    tkc0 = web3.eth.contract(address=token0, abi=ERC20ABI)
    tkc1 = web3.eth.contract(address=token1, abi=ERC20ABI)
    decimal0 = tkc0.functions.decimals().call()
    decimal1 = tkc1.functions.decimals().call()
    print(decimal0, decimal1, "Decimals")
    price =reserves[1] / reserves[0]
    print(price, "Price WETH")

token_price()