# coding=utf-8
from pyperp.providers import ApiProvider
from web3 import Web3
from pyperp.contracts.types import (
    OpenOrderInfo,
    FundingGrowth
)
from typing import List
import logging
from hexbytes import HexBytes


class UniV3Pool:

    def __init__(
            self,
            poolAddr: str,
            provider: ApiProvider
    ):
        '''
        Initialize provider.
        Arguments:
        provider - an object of class derived from ApiProvider
        '''
        self._provider = provider
        self.wallet = self._provider.account
        self.logger = logging.getLogger("UniV3Pool")

        self.logger.info("Loading UniV3Pool contract")
        uniV3_pool_meta = self._provider.load_meta("vBTCvUSDUniswapV3Pool")
        self.uniV3_pool = self._provider._api.eth.contract(
            address=poolAddr,
            abi=uniV3_pool_meta["abi"]
        )
        self.logger.info("UniV3Pool contract loaded")

    def get_mark_price(self):
        return self.uniV3_pool.functions.slot0().call()
