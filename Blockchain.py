import hashlib
import datetime
class Block:
    

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)

    def calc_hash(self, data):
        sha = hashlib.sha256()
        hash_str = data.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()


class LinkedList:
    def __init__(self):
        self.head = None
        self.last = None

    def append(self, timestamp, data):
        if not self.head:
            self.head = Block(timestamp, data, 0)
            self.last = self.head
        else:
            temp = self.last
            self.last = Block(timestamp, data, temp)
            self.last.previous_hash = temp

def get_utc_time():
    utc = datetime.datetime.utcnow()
    return utc.strftime("%d/%m/%Y %H:%M:%S")

block01 = Block(get_utc_time(), "Say my name", 10)
print(block01.data)
print(block01.hash)
print(block01.timestamp)

block02 = Block(get_utc_time(), "data", 10)
print(block02.data)
print(block02.hash)
print(block02.timestamp)


block03 = Block(get_utc_time(), "", 10)  #empty 
print(block03.data)
print(block03.hash)
print(block03.timestamp)

