import time


def getDeadline(expiry_seconds: int):
    return int(time.time()) + expiry_seconds


# address: uniswapV3
# baseAddress: vPair
# quoteAddress: vUSD
PERPV2_PAIR_LIST = [
    {
        "address": '0x6c0bC93A4208EB1648AF4ED44Cb3b4df9547B42B',
        "baseAddress": '0x34235C8489b06482A99bb7fcaB6d7c467b92d248',
        "baseSymbol": 'vAAVE',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x05B552C0a787c228624b389D51eB4277e1F0F348',
        "baseAddress": '0x9d34F1D15C22e4C0924804e2a38cBe93DFB84bc2',
        "baseSymbol": 'vAPE',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0xb98e6912aE77c643957eD51dCF755895eC4BC6b4',
        "baseAddress": '0x5f714B5347f0b5de9F9598E39840E176CE889b9c',
        "baseSymbol": 'vATOM',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x14Bc698Fdc368f2487d3eaD12DFF458E7c272047',
        "baseAddress": '0x5FAa136Fc58B6136fFDAeAAC320076C4865c070F',
        "baseSymbol": 'vAVAX',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0xf4d40ebCBf7063D4ff56C6Df0179a86287C648dE',
        "baseAddress": '0xb6599Bd362120Dc70D48409B8a08888807050700',
        "baseSymbol": 'vBNB',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0xC64f9436f8Ca50CDCC096105C62DaD52FAEb1f2e',
        "baseAddress": '0x86f1e0420c26a858fc203A3645dD1A36868F18e5',
        "baseSymbol": 'vBTC',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x6e39aCC0Dd292a70D92c447ebCcB8728f4eD5FE4',
        "baseAddress": '0x7161C3416E08AbAa5cd38E68D9A28E43a694e037',
        "baseSymbol": 'vCRV',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x36B18618c4131D8564A714fb6b4D2B1EdADc0042',
        "baseAddress": '0x8C835DFaA34e2AE61775e80EE29E2c724c6AE2BB',
        "baseSymbol": 'vETH',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0xD26ffdDE6c0DAaAbEB0a6806221c6b9fE7519bdf',
        "baseAddress": '0x7EAdA83e15AcD08d22ad85A1dCE92E5A257Acb92',
        "baseSymbol": 'vFLOW',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0xAeC0Bf409BB28eFe308108D400034650C4d9eC75',
        "baseAddress": '0x2dB8d2DB86cA3a4C7040E778244451776570359B',
        "baseSymbol": 'vFTM',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x008B996FD9E7e6d974D03A834a9dBBFcd74689A2',
        "baseAddress": '0x2F198182eC54469195a4A06262a9431A42462373',
        "baseSymbol": 'vLINK',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x4d7C361d7758107BDb88e4d36EF5ac5d85f8c6Fa',
        "baseAddress": '0xB24F50Dd9918934AB2228bE7A097411ca28F6C14',
        "baseSymbol": 'vLUNA',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x6f59c163AD6cC896145aF7D5922d1eAE174A1BCc',
        "baseAddress": '0xBe5de48197fc974600929196239E264EcB703eE8',
        "baseSymbol": 'vMATIC',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x2534D4f1325aA7D3FC8D5d14f224e5c587a719b0',
        "baseAddress": '0x3Fb3282e3BA34A0Bff94845f1800Eb93CC6850d4',
        "baseSymbol": 'vNEAR',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x2F449bD78a72B18f8758aC38c3FF8dcB094416f6',
        "baseAddress": '0x77d0cc9568605bFfF32F918C8FFaa53F72901416',
        "baseSymbol": 'vONE',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0x86f03C6E26B0488b6e39b34d7f10D843ae8e3d1b',
        "baseAddress": '0x9482AaFdCed6b899626f465e1FA0Cf1B1418d797',
        "baseSymbol": 'vPERP',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0xE4A1645dde99c20D126c24B8DD1d1a4Bc4a88e4C',
        "baseAddress": '0x333b1eA429a88d0dd48cE7C06C16609CD76F43A8',
        "baseSymbol": 'vSAND',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
    {
        "address": '0xf993cc412eDF1257F3e771Bb744645daF4c19b14',
        "baseAddress": '0x151Bb01c79F4516c233948D69daE39869BCcB737',
        "baseSymbol": 'vSOL',
        "quoteAddress": '0xC84Da6c8ec7A57cD10B939E79eaF9d2D17834E04',
        "quoteSymbol": 'vUSD'
    },
]


def get_pair_addr_by_name(name):
    # XXX-USD
    pair_name = "v" + name.split("-")[0].upper()
    for pair_info in PERPV2_PAIR_LIST:
        if pair_info["baseSymbol"] == pair_name:
            return pair_info["address"], pair_info["baseAddress"]
    raise Exception("{} not found".format(name))


def get_pair_name_by_addr(addr):
    for pair_info in PERPV2_PAIR_LIST:
        if pair_info["address"] == addr or pair_info["baseAddress"] == addr:
            return pair_info["baseSymbol"][1:] + "-USD"
    raise Exception("{} not found".format(addr))
