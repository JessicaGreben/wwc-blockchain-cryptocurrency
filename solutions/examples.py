# import the solution code from step3 to use here
import step3 as blockchain

from datetime import datetime


# Example 1: My first blockchain storing transactional data

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
my_first_blockchain = blockchain.Blockchain(genesis_block)

# a new transaction is created
new_transaction_data = {
    "to": '5KJvsngHeMpm884wtkJNzQGaCErckhHJBGFsvd3VyK5qMZXj3hS',
    "from": 'khHJBGFsvd3JNzQGaCS5KJvsnErcVyK5qMZXj3hgHeMpm884wtk',
    "value": "5",
    "timestamp": now(),

}

# the transaction is added to the blockchain 
# by creating a new block to store the transactional data
new_block = my_first_blockchain.create_block(new_transaction_data)
my_first_blockchain.add_block_to_chain(new_block)

# printing out the blocks of the blockchain
# shows that there are two blocks being stored:
# the genesis block and the new transaction block
print 'Printing out the blocks stored in my first blockchain:'
print my_first_blockchain.blocks



# Example 2: My second blockchain storing data about my favorite quotes.

now = datetime.utcnow
previous_block_hash = "I am number 1!"
genesis_block_data = {
    "favorite_quote": "\nNo one puts Baby in a corner.",
    "timestamp": now(),
}

genesis_block = blockchain.Block(now(), 
    previous_block_hash, 
    genesis_block_data,
)

# create the blockchain with the genesis block
my_fav_quote_blockchain = blockchain.Blockchain(genesis_block)

# a new transaction is created
new_fav_quote_data = {
    "favorite_quote": "To be or not to be? That is the question.",
    "timestamp": now(),
}

# the the quote to the blockchain
new_block = my_fav_quote_blockchain.create_block(new_fav_quote_data)
my_fav_quote_blockchain.add_block_to_chain(new_block)

# printing out the favorite quotes stored in the blocks of the blockchain
for quote in my_fav_quote_blockchain.blocks:
    print quote.data.get('favorite_quote')
