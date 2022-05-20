# coding=utf-8
from pyperp.providers import ApiProvider
import logging


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
        self.logger = logging.getLogger("UniV3Pool")

        self.logger.info("Loading UniV3Pool contract")
        uniV3_pool_meta = self._provider.load_meta("vBTCvUSDUniswapV3Pool")
        self.uniV3_pool = self._provider._api.eth.contract(
            address=poolAddr,
            abi=uniV3_pool_meta["abi"]
        )
        self.logger.info("UniV3Pool contract loaded")
        self.pow_constant = 2 ** 96

    def get_mark_price(self):
        # sqrtPriceX96
        return (self.uniV3_pool.functions.slot0().call()[0] / self.pow_constant) ** 2
