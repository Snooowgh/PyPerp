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


class PairPool:

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
        self.logger = logging.getLogger("PairPool")

        self.logger.info("Loading PairPool contract")
        pair_pool_meta = self._provider.load_meta("vBTC")
        self.pair_pool = self._provider._api.eth.contract(
            address=poolAddr,
            abi=pair_pool_meta["abi"]
        )
        self.logger.info("PairPool contract loaded")
