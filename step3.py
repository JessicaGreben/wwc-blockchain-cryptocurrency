# Task: Validate a block

# A Blockchain should also have a mechanism to confirm a block is valid.  A block is valid when these criteria are met:
# * the previous hash attribute of the current block matches the current hash of the previous block
# * the index of the previous block is one less than the index of the current block


class Blockchain(object):
    """
    """
    def __init__(self, blocks=[]):
        """
        """
        self.blocks = blocks

    def create_block(self):
        """
        """

    def get_recent_block(self):
        """
        """

    def is_block_valid(self, block):
        """
        """