# Task: Implement a `validate_block` method in the `Blockchain` class.
# A Blockchain should also have a mechanism to confirm a block is valid.  Implement a validation function that check that a block is valid.
# A block is valid when:
# * the previous hash attribute of the current block matches the current hash of the previous block


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

    def is_valid_block(self):
        # TODO: write code to do this