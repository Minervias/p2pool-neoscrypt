import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack

P2P_PREFIX = 'b93a2a3c'.decode('hex')
P2P_PORT = 14520
ADDRESS_VERSION = 76
RPC_PORT = 8818
RPC_CHECK = defer.inlineCallbacks(lambda daemon: defer.returnValue(
  'innovaaddress' in (yield daemon.rpc_help()) and
  not (yield daemon.rpc_getinfo())['testnet']))
SUBSIDY_FUNC = lambda height: 20*100000000 >> (height + 1)//262800
POW_FUNC = lambda data: pack.IntType(256).unpack(__import__('neoscrypt').getPoWHash(data))
BLOCK_PERIOD = 120
SYMBOL = 'INN'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.getcwd(), 'data') if platform.system() == 'Windows' else os.path.expanduser('~/.innovacoin'), 'innovacoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'http://explorer.innovacoin.info/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'http://explorer.innovacoin.info/address/'
TX_EXPLORER_URL_PREFIX = 'http://explorer.innovacoin.info/tx/'
SANE_TARGET_RANGE = (2**256 - 1 >> 30, 2**256 - 1 >> 12)
DUMB_SCRYPT_DIFF = 2**16
DUST_THRESHOLD = 0.1e8
