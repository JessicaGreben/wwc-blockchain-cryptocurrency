## Welcome

Welcome to the Portland Women Who Code: Bitcoin, Cryptocurrency and Blockchain Workshop.

For this exercise we will be implementing a simple Blockchain from scratch. We will build a simple Blockchain with the goal of understanding what the basic features are that make up a blockchain database.

## Setup

The following exercise assumes you have a text editor installed and are able to write code in a language of your choice, but the solutions are written in Python and you can reference this [blog on creating a Blockchain](https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54) with a similar exercise that has solutions written in JavaScript..  Feel free to pair with others while working through this exercises.


### Step 1 - What is a Block in a Blockchain?

In the presentation we learned that a Blockchain is a database, which is just a grouping of data organized in a particular way.  A blockchain database organizes its data in blocks.

A block is a container data structure that permanently stores data that cannot be altered or removed. A block is primarily made of a header and a long list of transactions.

#### Task: Implement a `Block` class.

Implement a `Block` class with the following attributes:
* timestamp
* hash of the previous block
* transactional data


### Step 2 - Lets Chain the Blocks Together

The Blockchain data strucutre is an ordered list of blocks.  Blocks are linked "back", each pointing to the previous block in the chain creating an immutable data structure that is very difficult to alter maliciously.

#### Task: Implement a `Blockchain` class.

A Blockchain should have the following attributes:
* a data structure to store blocks 
* the first block should be hardcoded, its called the genesis block

A [genesis block](https://en.bitcoin.it/wiki/Genesis_block) is the first block of a block chain. The genesis block is typically hardcoded into the blockchain.

A Blockchain should be able to perform the following functions:
* create a new block and add it to the blocks attribute
* get the most recent block in from the blocks attribute
* There is a hash function provided that can be used to generate the hash of any block.

A [hash function](https://en.wikipedia.org/wiki/Hash_function) is a way to turn any amount of data or any size data into a constant size. The values returned by a hash function are called hash values, hash codes, digests, or simply hashes. One example of a use case is a data structure called a hash table, used for rapid data lookup. 

In the hash function provided, you can see that we are hashing the previous blocks hash. This is an important topic, but also pretty detailed so we don't want to go into the details here. If you are interested in diving deep to understand this, see the resources listed at the bottom of this readme. However at a high level, hashing the blocks provides a secure mechanism to confirm the integrity of the Blockchain data.


### Step 3 - Validate a Block

#### Task: Implement a `validate_block` method in the `Blockchain` class.

When we add a new block to the block chain, check to make sure that this previous block hash still matches the current block's attribute that stores the hash of the previous block.

A Blockchain should also have a mechanism to confirm a block is valid.  Implement a validation function that check that a block is valid.
A block is valid when:
* the previous hash attribute of the current block matches the current hash of the previous block


## Beyond the workshop:

Topics not convered in this workshop that you may want to explore outside of this workshop:

* Selecting the Longest Chain
* Consensus Protocol including Proof of Work
* Public Key Encryption and Digital Signatures
* Communicating with other nodes; peer-to-peer networking


## Where to go to learn more:

[Bitcoin Whitepaper](https://bitcoin.org/bitcoin.pdf)

[Mastering Bitcoin Book](http://chimera.labs.oreilly.com/books/1234000001802/index.html)

[Coursera - Bitcoin and Cryptocurrency Technology](https://www.coursera.org/learn/cryptocurrency)

[A blockchain in 200 lines of code](https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54)

[Learn Blockchains By Building One](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)

