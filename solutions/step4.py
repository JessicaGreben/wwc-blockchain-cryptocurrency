# Task: Implement a `validate_block` method in the `Blockchain` class.

# A Blockchain should also have a mechanism to confirm a block is valid.  A block is valid when these criteria are met:
# - the previous hash attribute of the current block matches the current hash of the previous block
# - the index of the previous block is one less than the index of the current block
# - hashing the current block matches the current_hash attribute of the block

# Once this `validate_block` method is implemented, update the Blockchain.add_block_to_chain 
#   method to include a validation check. If the validation check fails, 
#   then do not add the block to the block chain.


from datetime import datetime


class Block(object):
    """
    Stores data and metadata about transactions.
    """
    def __init__(self, timestamp, index, previous_hash, data):
        self.timestamp = timestamp
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.simple_hash_block()

    def simple_hash_block(self):
        """
        Format the block data into a unified size.
        """
        summed = 0
        hash_content = str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.data)

        for char in list(hash_content):
            summed += ord(char)

        current_hash = summed % 1000
        self.current_hash = current_hash
        return current_hash


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
        index = len(self.blocks)
        previous_block = get_recent_block()
        data = data
        new_block = Block(timestamp, index, previous_block, data)
        return new_block

    def add_block_to_chain(self, new_block):
        """
        Add the new block to the existing blocks data structure if the new block is valid.
        """
        previous_block = get_recent_block()
        if block.is_block_valid(new_block, previous_block):
            blocks.append(new_block)
        else:
            print 'Not a valid block, cannot add this block to the blockchain'
            return False
        return blocks

    def is_block_valid(self, current_block, previous_block):
        """
        Confirm the block is valid.
        A block is valid when:
        - the previous_hash attribute matches the hash of the actual previous block
        - the index of the previous block is one less than the current block
        """
        if current_block.previous_hash != previous_block.current_hash:
            print 'Invalid previous hash'
            return False
        elif current_block.index != previous_block.index + 1:
            print 'Invalid index'
            return False
        elif current_block.hash != current_block.simple_hash_block():
            print 'Invalid current hash'
            return False
        else:
            return True
