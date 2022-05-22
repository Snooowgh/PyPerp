# coding=utf-8
from pyperp.providers import ApiProvider


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
        pair_pool_meta = self._provider.load_meta("vBTC")
        self.pair_pool = self._provider._api.eth.contract(
            address=poolAddr,
            abi=pair_pool_meta["abi"]
        )

    def get_twap_index_price(self):
        interval = 15 * 60
        return self.pair_pool.functions.getIndexPrice(interval).call() / 10 ** 18

    def get_index_price(self):
        interval = 0
        return self.pair_pool.functions.getIndexPrice(interval).call() / 10 ** 18
