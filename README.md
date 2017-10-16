## Welcome

Welcome to the Portland Women Who Code Bitcoin, Cryptocurrency and Blockchain Workshop.

For this exercise we will be implementing a Blockchain from scratch. We will build a simple Blockchain with the goal of understanding what the basic features are that make up a blockchain database.

## Setup

The following exercise assumes you have a text editor installed and are able to write code in a language of your choice (the solutions are written in Python).  Feel free to pair with others while working through these exercises.

### Step 1 - What is a Block in a Blockchain?

In the presentation we learn that a Blockchain is a database, which is just a grouping of data organized in a particular way.  A blockchain database organizes its data in blocks.  

A block is a container data structure that permanently stores records that cannot be altered or removed. A block is primarily made of a header and a long list of transactions.

#### Task: Implement a `Block` class. 

A Block should have the following attributes:
* timestamp
* index of position in the blockchain
* pointer to the previous block
* transactional data

A Block should be able to perform the following actions:
* hash itself


### Step 2 - Lets Chain the Blocks Together

The Blockchain data strucutre is a linked list of blocks.  Blocks are linked "back", each pointing to the previous block in the chain creating an immutable data structure that is nearly impossible to alter maliciously. 

#### Task: Implement a `Blockchain` class.

A Blockchain should have the following attributes:
* blocks
* a single genesis block

A Blockchain should be able to perform the following functions:
* create a new block and add it to the blockchain
* get the most recent block in the blockchain


### Step 3 - Validate a Block

A Blockchain should also have a mechanism to confirm a block is valid.  A block is valid when these criteria are met:
* the previous hash attribute of the current block matches the current hash of the previous block
* the index of the previous block is one less than the index of the current block

## Beyond the workshop:

Topics not convered in this workshop that you may want to explore:

* Consensus Protocol
* Longest Chain
* Networking details of the Bitcoin network

## Where to go to learn more:

[Mastering Bitcoin Book](http://chimera.labs.oreilly.com/books/1234000001802/index.html)

[Coursera - Bitcoin and Cryptocurrency Technology](https://www.coursera.org/learn/cryptocurrency)

Blog this workshop was based on: [A blockchain in 200 lines of code](https://medium.com/@lhartikk/a-blockchain-in-200-lines-of-code-963cc1cc0e54)

