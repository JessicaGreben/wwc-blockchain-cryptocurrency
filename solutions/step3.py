# Task: Implement a simple hash function

# Write a method called `simple_hash` that accepts a Block object as a parameter.  Remember the current block

# The hash should perform the following steps:
# - convert each character of the string into its ascii value
# - sum up these values
# - perform the modulus operation like so: sum % 1000
# - return that value

# Once the simple hash function is implemented then update the existing code to do the following:
# - in the Block class, instead of a previous_block attribute, change it to previous_hash attribute so that this pointer is actually a hash pointer now
# - in the initialzation of the Block class add an instantiation of the simple
#   hash method so that we hash the contents of the block and store that data on the block itself.
# - in the Blockchain.create_block method, update previous_block to previous_hash


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
        Adds a current_hash attribute to the Block.
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
        previous_hash = get_recent_block().current_hash
        data = data
        new_block = Block(timestamp, index, previous_hash, data)
        return new_block

    def add_block_to_chain(self, new_block):
        """
        Add the new block to the existing blocks data structure.
        """
        blocks.append(new_block)
        return blocks
