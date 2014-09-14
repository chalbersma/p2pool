from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['altcoin']
SHARE_PERIOD = 30 # seconds
CHAIN_LENGTH = 24*60*60//10 # shares
REAL_CHAIN_LENGTH = 24*60*60//10 # shares
TARGET_LOOKBEHIND = 200 # shares
SPREAD = 3 # blocks
IDENTIFIER = 'fc70035c7a81bc6a'.decode('hex')
PREFIX = '2472ef181efcd37a'.decode('hex')
P2P_PORT = 8558
MIN_TARGET = 0
MAX_TARGET = 2**256//2**32 - 1
PERSIST = False
WORKER_PORT = 8559
BOOTSTRAP_ADDRS = '104.131.60.126'.split(' ')
ANNOUNCE_CHANNEL = '#atcp2pool'
VERSION_CHECK = lambda v: 50700 <= v < 60000 or 60010 <= v < 60100 or 60400 <= v
VERSION_WARNING = lambda v: 'Upgrade Bitcoin to >=0.8.5!' if v < 80500 else None
