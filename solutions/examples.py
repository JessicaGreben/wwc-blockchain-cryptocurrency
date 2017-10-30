# import the solution code from step3 to use here
import step3 as blockchain

from datetime import datetime

# variables that will be used to create the genesis block
now = datetime.utcnow
previous_block_hash = "No previous block since I'm the first block"
genesis_block_data = {
    "to": None,
    "from": None,
    "value": "No value, I'm the genesis block",
    "timestamp": now(),
}


# create the genesis block, which will be the first block in the blockchain
genesis_block = blockchain.Block(now(), 
    previous_block_hash, 
    genesis_block_data,
)

# create the blockchain with the genesis block
my_blockchain = blockchain.Blockchain(genesis_block)

# a new transaction is created
new_transaction_data = {
    "to": '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
    "from": 'khHJBGFsvd3JNzQGaCS5KJvsnErcVyK5qMZXj3hgHeMpm884wtk',
    "value": "5",
    "timestamp": now(),

}

# the transaction is added to the blockchain 
# by creating a new block to store the transactional data
new_block = my_blockchain.create_block(new_transaction_data)
my_blockchain.add_block_to_chain(new_block)

# printing out the blocks of the blockchain
# shows that there are two blocks being stored:
# the genesis block and the new transaction block
print my_blockchain.blocks
