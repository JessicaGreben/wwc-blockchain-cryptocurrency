# Task: Implement a `Blockchain` class.

# A Blockchain should have the following attributes:
# * a data structure to store blocks 
# * the first block should be hardcoded, its called the genesis block

# A Blockchain should be able to perform the following functions:
# * create a new block and add it to the blocks attribute
# * get the most recent block in from the blocks attribute
# * There is a hash function provided that can be used to generate the hash of any block.


from datetime import datetime

import hashlib


class Block(object):
    """
    Stores data and metadata about transactions.
    """
    def __init__(self, timestamp, previous_block, data):
        self.timestamp = timestamp
        self.previous_block = previous_block
        self.data = data


class Blockchain(object):
    """
    Links together blocks of data.
    """
    def __init__(self, genesis_block):
        self.blocks = [genesis_block]

    def get_recent_block(self):
        """
        Return the last item in blocks.
        """
        return self.blocks[-1]

    def create_block(self, data):
        """
        Create a new block with the following arguments:
        - timestamp should be the current time
        - index should be the position of the new block in the list of blocks
        - previous block should point to the block before it in the list of blocks. This pointer is what creates the "chain" of the blockchain.
        - data can be any type of data. In the case of Bitcoin, data is transactional data.
        """
        timestamp = datetime.utcnow()
        previous_block = get_recent_block()
        previous_block_hash = self.hash_block(previous_block)
        data = data
        new_block = Block(timestamp, previous_block_hash, data)
        return new_block

    def add_block_to_chain(self, new_block):
        """
        Add the new block to the existing blocks data structure.
        """
        blocks.append(new_block)
        return blocks

    def hash_block(block):
        """
        Hash the contents of the current block with the 
        previous block's hash.
        """
        hash_content = str(block.timestamp) + block.previous_hash + block.data
        return hashlib.sha256(hash_content).hexdigest()

















        
