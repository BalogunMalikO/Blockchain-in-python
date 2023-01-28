import hashlib
import random
import string
import json
import binascii
import datetime
import collections
import ecdsa
from datetime import datetime
from Crypto.Hash import SHA

#client is someone or a vendor that can be a reciever or a sender of a transactiion
class client:

    def __init__(self):
        #generating a private key
        sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)

        self._private_key = sk.to_string()
        self._public_key = sk.get_verifying_key().to_string()

    @property
    def identity(self):
      #this line is to convert the public key to an ascii standard using the binascii module
      return binascii.hexlify(self._public_key).decode('ascii')


class Transaction:

    def __init__(self, sender, recipient, value):
      self.sender = sender
      self.recipient =recipient
      self.value = value
      self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    def to_dict (self):

     identity = self.sender.identity

     return collections.OrderedDict({"sender": identity,
                                         "recipient": self.recipient,
                                          "value": self.value,
                                        "time": self.time,
                                         }
                                                              )



    def sign_transaction(self):
           sk = ecdsa.SigningKey.generate(curve=ecdsa.NIST256p)
           private_key = self.sender._private_key
           signer = sk.get_verifying_key().to_string()
           h = (str(self.to_dict()).encode('utf8'))
           h_signed = sk.sign(h)
           hashed_h= hashlib.sha256(h_signed)
           hex_h = hashed_h.hexdigest()
           # print(hex_h)
           # print(h)
           return binascii.hexlify(h_signed).decode('ascii')




malik = client()
ade = client()

t = Transaction(
    malik,
    ade.identity,
    5.0)



signature = t.sign_transaction()
# print(signature)


def display_transaction(transaction):
    for transaction in transactions:
        dict = transaction.to_dict()
        print("sender: " + dict['sender'])
        print('-----')
        print("recipient: " + dict['recipient'])
        print('-----')
        print("value: " + str(dict['value']))
        print('-----')
        print("time: " + str(dict['time']))
        print('-----')
transactions =[]

client_1 = client()
client_2 = client()
client_3 = client()
client_4 = client()

t1 = Transaction(
    client_1,
    client_2.identity,
    25.0
)

t1.sign_transaction()
transactions.append(t1)


t2 = Transaction(
    client_1,
    client_3.identity,
    2.0
)
t2.sign_transaction()
transactions.append(t2)

t3 = Transaction(
    client_2,
    client_1.identity,
    3.0

)
t3.sign_transaction()
transactions.append(t3)

t4 = Transaction(
     client_4,
     client_2.identity,
     40.0        )

t4.sign_transaction()
transactions.append(t4)

# for transaction in transactions:
#     display_transaction(transaction)

print("-------------------")

class Block:
    def __init__(self):
       self.verified_transactions =[]
       self.previous_block_hash = ""
       self.nonce = ""





last_block_hash = ""

giver = client()


t0 = Transaction(
    "Genesis",
    giver.identity,
    500.0
)
block0 = Block()

block0.previous_block_hash = None
nonce = None

block0.verified_transactions.append (t0)

digest = hash (block0)
last_block_hash = digest

print("staring out now.......")


Berrycoins = []

def dump_blockchain (self):
    print("Number of blocks in the chain:" ""+ str(len(self)))
    for x in range (len(Berrycoins)):
        block_temp = Berrycoins[x]
        print("block#" + str(x))

        for transaction in block_temp.verified_transactions:
           display_transaction(transaction)
           print("--------------------")
        print("===================================")


Berrycoins.append (block0)


def sha256(message):
    return hashlib.sha256(message.encode('ascii')).hexdigest()

def mine(message, difficulty=0):
    assert difficulty >= 0
    prefix = '0' * difficulty

    for i in range(10000):
        hex_digest = sha256(str(hash(message)) + str(i))
        if hex_digest.startswith(prefix):
            print ("After " + str(i) + " Nonce found Hash: " + hex_digest)

            return hex_digest
        # print(hex_digest)

last_transaction_index = 0
Genesis_hash = "0" * 64
print (Genesis_hash)

block = Block()
for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    # validate transaction

    block.verified_transactions.append(temp_transaction)

last_transaction_index +=1
block.previous_block_hash = last_block_hash
block.nonce = mine(block, 2)
digest = hash(block)
Berrycoins.append(block)
last_block_hash = digest


block = Block()
for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    # validate transaction

    block.verified_transactions.append(temp_transaction)
last_transaction_index +=1
block.previous_block_hash = last_block_hash
block.nonce = mine(block, 2)
digest = hash(block)
Berrycoins.append(block)
last_block_hash = digest

block = Block()
for i in range(3):
    temp_transaction = transactions[last_transaction_index]
    # validate transaction

    block.verified_transactions.append(temp_transaction)

last_transaction_index +=1
block.previous_block_hash = last_block_hash
block.nonce = mine(block, 2)
digest = hash(block)
Berrycoins.append(block)
last_block_hash = digest

dump_blockchain(Berrycoins)
