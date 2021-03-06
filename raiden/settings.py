from eth_utils import denoms, to_hex

INITIAL_PORT = 38647

RPC_CACHE_TTL = 600
CACHE_TTL = 60
GAS_LIMIT = 10 * 10**6
GAS_LIMIT_HEX = to_hex(GAS_LIMIT)
GAS_PRICE = denoms.shannon * 20

DEFAULT_TRANSPORT_RETRIES_BEFORE_BACKOFF = 5
DEFAULT_TRANSPORT_THROTTLE_CAPACITY = 10.
DEFAULT_TRANSPORT_THROTTLE_FILL_RATE = 10.
DEFAULT_TRANSPORT_UDP_RETRY_INTERVAL = 1.
# matrix gets spammed with the default retry-interval of 1s, wait a little more
DEFAULT_TRANSPORT_MATRIX_RETRY_INTERVAL = 5.

DEFAULT_REVEAL_TIMEOUT = 10
DEFAULT_SETTLE_TIMEOUT = 500
DEFAULT_RETRY_TIMEOUT = 0.5
DEFAULT_POLL_TIMEOUT = 180
DEFAULT_JOINABLE_FUNDS_TARGET = 0.4
DEFAULT_INITIAL_CHANNEL_TARGET = 3
DEFAULT_WAIT_FOR_SETTLE = True
DEFAULT_NUMBER_OF_CONFIRMATIONS_BLOCK = 5
DEFAULT_CHANNEL_SYNC_TIMEOUT = 5

DEFAULT_NAT_KEEPALIVE_RETRIES = 5
DEFAULT_NAT_KEEPALIVE_TIMEOUT = 5
DEFAULT_NAT_INVITATION_TIMEOUT = 15

DEFAULT_SHUTDOWN_TIMEOUT = 2

ORACLE_BLOCKNUMBER_DRIFT_TOLERANCE = 3
ETHERSCAN_API = 'https://{network}.etherscan.io/api?module=proxy&action={action}'

EXPECTED_CONTRACTS_VERSION = '0.3.0'
