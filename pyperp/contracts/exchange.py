# coding=utf-8
from pyperp.providers import ApiProvider


class Exchange:

    def __init__(
            self,
            provider: ApiProvider
    ):
        '''
        Initialize provider.
        Arguments:
        provider - an object of class derived from ApiProvider
        '''
        self._provider = provider
        exchange_meta = self._provider.load_meta("Exchange")
        self.exchange = self._provider._api.eth.contract(
            address=exchange_meta["address"],
            abi=exchange_meta["abi"]
        )

    def get_pending_funding_payment(self, trader):
        return self.exchange.functions.getPendingFundingPayment(trader).call()

    def get_all_pending_funding_payment(self, trader, baseToken):
        return self.exchange.functions.getAllPendingFundingPayment(trader, baseToken).call()
