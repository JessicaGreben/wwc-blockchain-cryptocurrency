## Welcome

Welcome to the Portland Women Who Code Bitcoin, Cryptocurrency and Blockchain Workshop.

For this exercise we will be implementing a Blockchain from scratch. We will build a simple Blockchain with the goal of understanding what the basic features are that make up a blockchain database.

## Setup

The following exercise assumes you have a text editor installed and are able to write code in a language of your choice (the solutions are written in Python).  Feel free to pair with others while working through these exercises.


### Step 1 - What is a Block in a Blockchain?

In the presentation we learn that a Blockchain is a database, which is just a grouping of data organized in a particular way.  A blockchain database organizes its data in blocks.  

A block is a container data structure that permanently stores records that cannot be altered or removed. A block is primarily made of a header and a long list of transactions.

The "data" is typically a list of transactions in the case of Bitcoin, but in the real world it can also be anything.

#### Task: Implement a `Block` class.

A Block should have the following attributes:
* timestamp
* index of position in the blockchain
* pointer to the previous block
* transactional data

Later in Step 3 we will implement a hash function to hash the block contents.


### Step 2 - Lets Chain the Blocks Together

The Blockchain data strucutre is a linked list of blocks.  Blocks are linked "back", each pointing to the previous block in the chain creating an immutable data structure that is nearly impossible to alter maliciously.

#### Task: Implement a `Blockchain` class.

A Blockchain should have the following attributes:
* a data structure to store blocks 
* the first block should be hardcoded, its called the genesis block

A [genesis block](https://en.bitcoin.it/wiki/Genesis_block) is the first block of a block chain. The genesis block is typically hardcoded into the blockchain.

A Blockchain should be able to perform the following functions:
* create a new block and add it to the blocks attribute
* get the most recent block in from the blocks attribute


### Step 3 - What is a hash function?

A [hash function](https://en.wikipedia.org/wiki/Hash_function) is a way to turn any amount of data or any size data into a constant size. The values returned by a hash function are called **hash values**, **hash codes**, **digests**, or **simply hashes**. One example of a use case is a data structure called a hash table, used in computer software for rapid data lookup. 

Hash functions are used all over in Blockchains. One place is data on the blockchain is “hashed” in each block. This allows a quick, secure mechanism to confirm the integrity of the Blockchain data.

#### Task: Implement a simple hash function

Write a method called `simple_hash` that accepts a Block object as a parameter.  Remember the current block

The hash should perform the following steps:
* convert each character of the string into its ascii value
* sum up these values
* perform the modulus operation like so: sum % 1000
* return that value

The real hash function used in Bitcoin is SHA256, you can learn more about that here.
Two of the biggest difference are collision, cryptographic hash.


### Step 4 - Validate a Block

#### Task: Implement a `validate_block` method in the `Blockchain` class.

A Blockchain should also have a mechanism to confirm a block is valid.  A block is valid when these criteria are met:
* the previous hash attribute of the current block matches the current hash of the previous block
* the index of the previous block is one less than the index of the current block


## Beyond the workshop:

Topics not convered in this workshop that you may want to explore:

* Consensus Protocol including Proof of Work
* Digital Signatures; Public Private Key Encryption
* Longest Chain
* Networking details of the Bitcoin network


## Where to go to learn more:

[Mastering Bitcoin Book](http://chimera.labs.oreilly.com/books/1234000001802/index.html)

[Coursera - Bitcoin and Cryptocurrency Technology](https://www.coursera.org/learn/cryptocurrency)

[A blockchain in 200 lines of code](https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54)

[Learn Blockchains By Building One](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)

