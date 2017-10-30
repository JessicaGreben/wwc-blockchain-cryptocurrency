# Task: Implement a `Blockchain` class.

# A Blockchain should have the following attributes:
# * a data structure to store blocks 
# * the first block should be hardcoded, its called the genesis block

# A Blockchain should be able to perform the following functions:
# * create a new block and add it to the blocks attribute
# * get the most recent block in from the blocks attribute
# * There is a hash function provided that can be used to generate the hash of any block.


class Blockchain(object):
    def __init__(self):

    def get_recent_block(self):

    def create_block(self):

    def add_block_to_chain(self):

    def hash_block(block):
    """
    """
    hash_content = str(block.index) + str(block.timestamp) + block.previous_hash + block.data
    return hashlib.sha256(hash_content).hexdigest()
