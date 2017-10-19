# Task: Implement a `Block` class. 

# A Block should have the following attributes:
# - timestamp
# - index of position in the blockchain
# - pointer to the previous block
# - tTask: Implement a `Block` class. 


class Block(object):
    """
    Stores data and metadata about transactions.
    """
    def __init__(self, timestamp, index, previous_block, data):
        self.timestamp = timestamp
        self.index = index
        self.previous_block = previous_block
        self.data = data