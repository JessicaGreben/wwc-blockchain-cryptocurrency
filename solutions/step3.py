# Task: Implement a `validate_block` method in the `Blockchain` class.
# A Blockchain should also have a mechanism to confirm a block is valid.  Implement a validation function that check that a block is valid.
# A block is valid when:
# * the previous hash attribute of the current block matches the current hash of the previous block

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
        previous_block = get_recent_block()
        if self.is_block_valid(new_block, previous_block):
            blocks.append(new_block)
        return blocks

    def hash_block(block):
        """
        Hash the contents of the current block with the 
        previous block's hash.
        """
        hash_content = str(block.timestamp) + block.previous_hash + block.data
        return hashlib.sha256(hash_content).hexdigest()

    def is_block_valid(self, current_block, previous_block):
        """
        Confirm the block is valid.
        A block is valid when:
        - the previous_hash attribute matches the hash of the actual previous block
        """
        if current_block.previous_hash != previous_block.current_hash:
            print 'Invalid previous hash'
            return False
        return True
