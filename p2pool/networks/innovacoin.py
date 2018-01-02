from p2pool.bitcoin import networks

# CHAIN_LENGTH = number of shares back client keeps
# REAL_CHAIN_LENGTH = maximum number of shares back client uses to compute payout
# REAL_CHAIN_LENGTH must always be <= CHAIN_LENGTH
# REAL_CHAIN_LENGTH must be changed in sync with all other clients
# changes can be done by changing one, then the other

PARENT = networks.nets['innovacoin']
SHARE_PERIOD = 24  # seconds
CHAIN_LENGTH = 60*60//10  # shares
REAL_CHAIN_LENGTH = 60*60//10  # shares
TARGET_LOOKBEHIND = 200  # shares
SPREAD = 15  # blocks
IDENTIFIER = '19FFDB6CEB80E13B'.decode('hex')  # Innova
PREFIX = '7B2861EB7F2BD772'.decode('hex')  # INN-Live
P2P_PORT = 14521
MIN_TARGET = 0
MAX_TARGET = 2**256//2**20 - 1
PERSIST = True
WORKER_PORT = 14520
BOOTSTRAP_ADDRS = 'inn.swiftpool.org'.split(' ')
ANNOUNCE_CHANNEL = '#p2pool-inn'
VERSION_CHECK = lambda v: True
VERSION_WARNING = lambda v: 'Upgrade Innovacoin to >= 0.6.6.0!' if v < 60600 else None
