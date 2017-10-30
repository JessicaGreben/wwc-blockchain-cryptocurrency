# Task: Implement a `Blockchain` class.

# A Blockchain should have the following attribute:
# * a data structure to store the blocks with the first block already created

# A Blockchain should be able to perform the following functions:
# * create a new block and add it to the blocks attribute
# * get the most recent block in from the blocks attribute
# * There is a hash function provided that can be used to generate the hash of any block.

import hashlib


class Block(object):
    def __init__():
        # TODO: copy the solution from step 1 here


class Blockchain(object):
    def __init__(self):
        # TODO: add the attribute of a blockchain here

    def get_recent_block(self):
        # TODO: write the code to implement this function

    def create_block(self):
        # TODO: write the code to implement this function

    def add_block_to_chain(self):
        # TODO: write the code to implement this function

    def hash_block(block):
        """
        Hash the contents of the current block with the previous block's hash.
        This creates the link in the blockchain that helps ensure the integrity fo the data.
        """
        hash_content = str(block.index) + str(block.timestamp) + block.previous_hash + block.data
        return hashlib.sha256(hash_content).hexdigest()
