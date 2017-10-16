# Task: Implement a `Block` class. 

# A Block should have the following attributes:
# * timestamp
# * index of position in the blockchain
# * pointer to the previous block
# * tTask: Implement a `Block` class. 

# A Block should have the following attributes:
# * timestamp
# * index of position in the blockchain
# * pointer to the previous block
# * transactional data

# A Block should be able to perform the following actions:
# * hash itselfransactional data

# A Block should be able to perform the following actions:
# * hash itself


class Block(object):
    """
    """
    def __init__(self, index, timestamp, previous_hash, data=None):
        """
        """
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.data = data

    def hash_block():
        """
        """