import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = '761afffd'.decode('hex')
P2P_PORT = 9336
ADDRESS_VERSION = 0
RPC_PORT = 9335
RPC_CHECK = defer.inlineCallbacks(lambda altcoind: defer.returnValue(
            (yield helper.check_genesis_block(altcoind, '000000007743eb8bccd550d0fb3da0abbfe955dbdf185783bedc7dbabf495d8e')) and
            not (yield altcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 512*100000000 >> (height + 1)//262141
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'ATC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Bitcoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Bitcoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.altcoin'), 'altcoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://atc.blockr.io/block/info'
ADDRESS_EXPLORER_URL_PREFIX = 'https://atc.blockr.io/address/info'
TX_EXPLORER_URL_PREFIX = 'https://atc.blockr.io/tx/info'
SANE_TARGET_RANGE = (2**256//2**32//1000000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.001e8
