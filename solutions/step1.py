# Task: Implement a `Block` class.

# Implement a `Block` class with the following attributes:
# * timestamp
# * hash of the previous block
# * transactional data


class Block(object):
    def __init__(self, timestamp, previous_hash, data):
        """
        Initialize a block with:
        - a timestamp of the block creation time
        - the hash of the block that came before it
        - the data or payload. For a cryptoocurrency, the data will be the transaction data
        """
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data
    