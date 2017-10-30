# Task: Implement a `validate_block` method in the `Blockchain` class.
# A Blockchain should also have a mechanism to confirm a block is valid.  Implement a validation function that check that a block is valid.
# A block is valid when:
# * the previous hash attribute of the current block matches the current hash of the previous block

import hashlib


class Block(object):
    def __init__():
        # TODO: copy the solution from step 1 here


class Blockchain(object):
    def __init__(self):
        # TODO: copy of the solution from step 2 here

    def get_recent_block(self):
        # TODO: copy of the solution from step 2 here

    def create_block(self):
        # TODO: copy of the solution from step 2 here

    def add_block_to_chain(self):
        # TODO: copy of the solution from step 2 here

    def hash_block(block):
        """
        Hash the contents of the current block with the previous block's hash.
        This creates the link in the blockchain that helps ensure the integrity fo the data.
        """
        hash_content = str(block.index) + str(block.timestamp) + block.previous_hash + block.data
        return hashlib.sha256(hash_content).hexdigest()

    def is_valid_block(self):
        # TODO: write the code to implement this function
